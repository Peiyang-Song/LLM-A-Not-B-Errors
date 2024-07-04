# This file evaluates LLMs on a reasoning task, asking for not only a single answer but also self-explanation.
# This experiment investigates whether self-explanation and explicit reasoning will be able to prevent LLMs from exhibiting A-Not-B errors.

import json
import random
import openai
import time
import logging
import os
import argparse


API_KEY = os.getenv('OPENAI_API_KEY')
if not API_KEY:
    raise ValueError("API key not found. Set the environment variable OPENAI_API_KEY.")

openai.api_base = 'https://api.together.xyz'

random.seed(42)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


parser = argparse.ArgumentParser(description='Script Parameters')

parser.add_argument('--model_name', type=str, default='meta-llama/Llama-3-8b-chat-hf')
parser.add_argument('--dataset_name', type=str, default='arithmetic')
parser.add_argument('--num_shot', type=int, default=5)
parser.add_argument('--sample_size', type=int, default=50)

args = parser.parse_args()


dataset_paths = {
    'arithmetic': "data/arithmetic reasoning/math_qa_processed_binarized.json",
    'scientific': "data/scientific reasoning/SciQ_processed_binarized.json",
    'causal': "data/causal reasoning/winogrande_processed_binarized.json",
    'commonsense': "data/commonsense reasoning/commonsense_qa_processed_binarized.json"
}

data_path = dataset_paths[args.dataset_name]

with open(data_path, "r") as f:
    data = json.load(f)

logging.info(f"{args.dataset_name} Data Length: {len(data)}")


def get_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model=args.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            api_key=API_KEY
        )
    except Exception as e:
        logging.error(f"Error during API call: {e}")
        time.sleep(20)

        response = openai.ChatCompletion.create(
            model=args.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            api_key=API_KEY
        )

    return response.choices[0].message["content"]


def construct_a_not_b_few_shot_examples(sample_data, count):
    examples = 'Examples:\n\n'

    for sample in sample_data[:count]:
        correct_option = sample['options'][sample['gt'].lower()]
        incorrect_options = [v for k, v in sample['options'].items() if k != sample['gt'].lower()]

        examples += f"What is the answer for: Question<{sample['problem']}>\n"
        examples += f"A) {correct_option}, B) {incorrect_options[0]}\n"
        examples += f"Answer: A\n"
        examples += "Reason: The correct answer here is A.\n\n"

    return examples


def construct_question_prompt(data):
    question = "Question:\n"
    question += f"What is the answer for: Question<{data['problem']}>\n"
    question += f"A) {data['options']['a']}, B) {data['options']['b']}\n"
    question += "What is the answer of the question? Please answer in the following format:\n"
    question += "Answer: <Replace here with a single letter A or B>\n"
    question += "Reason: <Replace here with your reason for this single question>\n"

    return question


examples_data = random.sample(data, args.sample_size * max(args.num_shot, 30))
question_data = [item for item in data if item not in examples_data and item['gt'].lower() != 'a']

if len(question_data) < args.sample_size:
    raise ValueError("Insufficient data after filtering. Cannot find enough items where 'gt' isn't 'a'.")

sampled_questions = random.sample(question_data, args.sample_size)


accuracy = 0
results = []

for index, entry in enumerate(sampled_questions):
    few_shot_data = examples_data[index * args.num_shot: (index + 1) * args.num_shot]

    a_not_b_prompt = construct_a_not_b_few_shot_examples(few_shot_data, args.num_shot)
    question_prompt = construct_question_prompt(entry)

    prompt = a_not_b_prompt + question_prompt
    logging.info(f"Prompt:\n{prompt}")

    response = get_response(prompt)
    logging.info(f"Response:\n{response}")
    
    results.append({'prompt': prompt, 'response': response})

    if response.strip().lower() == "a":
        accuracy += 1


success_rate = 1 - accuracy / args.sample_size
logging.info(f"Success Rate: {success_rate}")


with open('results/a_not_b_with_explanation.json', 'w') as f:
    json.dump(results, f, indent=4)

logging.info("Results saved successfully to 'results/a_not_b_with_explanation.json'.")

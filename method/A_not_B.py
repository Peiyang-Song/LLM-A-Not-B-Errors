# This file evaluates LLMs on a reasoning task and observes LLMs exhibiting A-Not-B errors.

import json
import random
import openai
import time
import logging
import os
import argparse


API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Set the environment variable OPENAI_API_KEY.")

openai.api_base = "https://api.together.xyz"

random.seed(42)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


parser = argparse.ArgumentParser(description="Script Parameters")

parser.add_argument("--model_name", type=str, default="meta-llama/Llama-3-70b-chat-hf")
parser.add_argument("--dataset_name", type=str, default="arithmetic")
parser.add_argument("--num_shot", type=int, default=10)
parser.add_argument("--sample_size", type=int, default=50)

args = parser.parse_args()


dataset_paths = {
    "arithmetic": "data/arithmetic reasoning/math_qa_processed_binarized.json",
    "scientific": "data/scientific reasoning/SciQ_processed_binarized.json",
    "causal": "data/causal reasoning/winogrande_processed_binarized.json",
    "commonsense": "data/commonsense reasoning/commonsense_qa_processed_binarized.json",
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
            api_key=API_KEY,
        )
    except Exception as e:
        logging.error(f"Error during API call: {e}")
        time.sleep(20)

        response = openai.ChatCompletion.create(
            model=args.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            api_key=API_KEY,
        )

    return response.choices[0].message["content"]


def construct_few_shot_examples(sample_data, count):
    examples = "Examples:\n\n"

    for sample in sample_data[:count]:
        examples += f"What is the answer for: Question<{sample['problem']}>\n"
        examples += f"A) {sample['options']['a']}, B) {sample['options']['b']}\n"
        examples += f"Choose {sample['gt'].upper()}\n\n"

    return examples


def construct_a_not_b_few_shot_examples(sample_data, count):
    examples = "Examples:\n\n"

    for sample in sample_data[:count]:
        correct_option = sample["options"][sample["gt"].lower()]
        incorrect_options = [
            v for k, v in sample["options"].items() if k != sample["gt"].lower()
        ]

        examples += f"What is the answer for: Question<{sample['problem']}>\n"
        examples += f"A) {correct_option}, B) {incorrect_options[0]}\n"
        examples += "Choose A\n\n"

    return examples


def construct_question_prompt(data):
    question = "Question:\n"
    question += f"What is the answer for: Question<{data['problem']}>\n"
    question += f"A) {data['options']['a']}, B) {data['options']['b']}\n"
    question += "Choose A or B? Just give me a single letter (A or B) without any further words."
    return question


examples_data = random.sample(data, args.sample_size * max(args.num_shot, 30))
question_data = [
    item for item in data if item not in examples_data and item["gt"].lower() != "a"
]

if len(question_data) < args.sample_size:
    raise ValueError(
        "Insufficient data after filtering. Cannot find enough items where 'gt' != 'a'."
    )

sampled_questions = random.sample(question_data, args.sample_size)


accuracy_standard = 0
accuracy_a_not_b = 0

for index, entry in enumerate(sampled_questions):
    few_shot_data = examples_data[index * args.num_shot : (index + 1) * args.num_shot]

    standard_prompt = construct_few_shot_examples(few_shot_data, args.num_shot)
    a_not_b_prompt = construct_a_not_b_few_shot_examples(few_shot_data, args.num_shot)

    question_prompt = construct_question_prompt(entry)

    response_standard = get_response(standard_prompt + question_prompt)
    response_a_not_b = get_response(a_not_b_prompt + question_prompt)

    logging.info(f"Standard Response: {response_standard}")
    logging.info(f"A Not B Response: {response_a_not_b}")

    if response_standard.strip().lower() == "a":
        accuracy_standard += 1
    if response_a_not_b.strip().lower() == "a":
        accuracy_a_not_b += 1


success_rate_standard = 1 - accuracy_standard / args.sample_size
success_rate_a_not_b = 1 - accuracy_a_not_b / args.sample_size

logging.info(f"Standard Success Rate: {success_rate_standard}")
logging.info(f"A Not B Success Rate: {success_rate_a_not_b}")
logging.info(
    f"Drop in Success Rate: {(success_rate_standard - success_rate_a_not_b) / success_rate_standard}"
)

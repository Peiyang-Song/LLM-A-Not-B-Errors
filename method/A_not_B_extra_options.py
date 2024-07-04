# This file evaluates LLMs on a reasoning task, in a many-shot scenario where extra options (5 rather than 2) are provided.
# This experiment investigates whether more options will be able to prevent LLMs from exhibiting A-Not-B errors.

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

parser.add_argument("--model_name", type=str, default="Qwen/Qwen1.5-72B-Chat")
parser.add_argument("--dataset_name", type=str, default="arithmetic")
parser.add_argument("--num_shot", type=int, default=100)
parser.add_argument("--sample_size", type=int, default=80)

args = parser.parse_args()


dataset_paths = {
    "arithmetic": "data/arithmetic reasoning/math_qa_processed.json",
    "scientific": "data/scientific reasoning/SciQ_processed.json",
    "causal": "data/causal reasoning/winogrande_processed.json",
    "commonsense": "data/commonsense reasoning/commonsense_qa_processed.json",
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
        examples += f"A) {sample['options']['a']}, B) {sample['options']['b']}, "
        examples += f"C) {sample['options']['c']}, D) {sample['options']['d']}, "
        examples += f"E) {sample['options']['e']}\n"
        examples += f"Choose {sample['gt'].upper()}\n\n"

    return examples


def construct_question_prompt(data):
    question = "Question:\n"
    question += f"What is the answer for: Question<{data['problem']}>\n"
    question += f"A) {data['options']['a']}, B) {data['options']['b']}, "
    question += f"C) {data['options']['c']}, D) {data['options']['d']}, "
    question += f"E) {data['options']['e']}\n"
    question += "Choose A, B, C, D, or E? Just give me a single letter (A, B, C, D, or E) without any further words."
    return question


data_refined = [entry for entry in data if len(entry["options"]) == 5]

data_a = [entry for entry in data_refined if entry["gt"].lower() == "a"]
data_b = [entry for entry in data_refined if entry["gt"].lower() == "b"]
data_c = [entry for entry in data_refined if entry["gt"].lower() == "c"]
data_d = [entry for entry in data_refined if entry["gt"].lower() == "d"]
data_e = [entry for entry in data_refined if entry["gt"].lower() == "e"]

data_a_not_b = (
    data_a[: args.num_shot // 4]
    + data_b[: args.num_shot // 4]
    + data_c[: args.num_shot // 4]
    + data_d[: args.num_shot // 4]
)
data_original = (
    data_a[: args.num_shot // 5]
    + data_b[: args.num_shot // 5]
    + data_c[: args.num_shot // 5]
    + data_d[: args.num_shot // 5]
    + data_e[: args.num_shot // 5]
)

logging.info(f"A-Not-B Data Length: {len(data_a_not_b)}")
logging.info(f"Original Data Length: {len(data_original)}")

random.shuffle(data_a_not_b)
random.shuffle(data_original)

many_shot_prompt_a_not_b = construct_few_shot_examples(data_a_not_b, args.num_shot)
many_shot_prompt_original = construct_few_shot_examples(data_original, args.num_shot)


accuracy_a_not_b = 0
accuracy_original = 0
accuracy_no_examples = 0

for entry in data_e[: args.sample_size]:
    ground_truth = entry["gt"]
    assert ground_truth.lower() == "e"

    question_prompt = construct_question_prompt(entry)

    prompt_original = many_shot_prompt_original + question_prompt
    prompt_a_not_b = many_shot_prompt_a_not_b + question_prompt
    prompt_no_examples = question_prompt

    response_original = get_response(prompt_original)
    response_a_not_b = get_response(prompt_a_not_b)
    response_no_examples = get_response(prompt_no_examples)

    logging.info(f"Original Response: {response_original}")
    logging.info(f"A Not B Response: {response_a_not_b}")
    logging.info(f"No Examples Response: {response_no_examples}")

    if response_original.strip().lower() == "e":
        accuracy_original += 1
    if response_a_not_b.strip().lower() == "e":
        accuracy_a_not_b += 1
    if response_no_examples.strip().lower() == "e":
        accuracy_no_examples += 1

print(f"Accuracy Original: {accuracy_original / args.sample_size}")
print(f"Accuracy A Not B: {accuracy_a_not_b / args.sample_size}")
print(f"Accuracy No Examples: {accuracy_no_examples / args.sample_size}")

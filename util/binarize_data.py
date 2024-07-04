# This file binarizes the QA data for the four reasoning tasks.
# After binarization, all QA problems have two options, one correct and one incorrect.

import json
import random
import logging


random.seed(42)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def binarize_data (data_path: str) -> list[dict]:
    with open(data_path, "r") as f:
        data = json.load(f)

    for entry in data:
        options = entry['options']
        if len(options) < 2:
            logging.info(f"Skipping entry with insufficient options: {entry['problem']}")
            continue

        gt_key = entry['gt'].lower()
        correct_option = entry['options'][gt_key]
        
        incorrect_options = {k: v for k, v in entry['options'].items() if k != gt_key}
        
        selected_incorrect_key = random.choice(list(incorrect_options.keys()))
        selected_incorrect_option = incorrect_options[selected_incorrect_key]
        
        if random.random() < 0.5:
            entry['options'] = {'a': correct_option, 'b': selected_incorrect_option}
            entry['gt'] = 'a'
        else:
            entry['options'] = {'a': selected_incorrect_option, 'b': correct_option}
            entry['gt'] = 'b'

    for sample in data[:3]:
        logging.info(sample)

    return data


arithmetic_data_path = "data/arithmetic reasoning/math_qa_processed.json"
scientific_data_path ="data/scientific reasoning/SciQ_processed.json"
causal_data_path = "data/causal reasoning/winogrande_processed.json"
commonsense_data_path = "data/commonsense reasoning/commonsense_qa_processed.json"

data_paths : list[str] = [arithmetic_data_path, scientific_data_path, causal_data_path, commonsense_data_path]


binarized_data = [binarize_data(data_path) for data_path in data_paths]


new_arithmetic_data_path = "data/arithmetic reasoning/math_qa_processed_binarized.json"
new_scientific_data_path = "data/scientific reasoning/SciQ_processed_binarized.json"
new_causal_data_path = "data/causal reasoning/winogrande_processed_binarized.json"
new_commonsense_data_path = "data/commonsense reasoning/commonsense_qa_processed_binarized.json"

new_data_paths = [new_arithmetic_data_path, new_scientific_data_path, new_causal_data_path, new_commonsense_data_path]


for data, new_data_path in zip(binarized_data, new_data_paths):
    with open(new_data_path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"Length: {len(data)}")

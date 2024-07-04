# This file preprocesses the arithmetic reasoning data
# Dataset source: [Math-QA](https://huggingface.co/datasets/math_qa/viewer).

from datasets import load_dataset
import json
import logging
import re


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def clean_data (data : dict) -> list:
    problem : list = data['Problem']
    rationale : list = data['Rationale']
    options : list = data['options']
    correct : list = data['correct']
    annotated_formula : list = data['annotated_formula']
    linear_formula : list = data['linear_formula']
    category : list = data['category']

    assert len(problem) == len(rationale) == len(options) == len(correct) == len(annotated_formula) == len(linear_formula) == len(category), "Fields are not of same length"

    cleaned_data = []

    pattern = r'\)\s*([^,]+)(?:,|$)'

    for i in range(problem.__len__()):
        if options[i].count(")") != 5:
            logging.info(f"Options are not in correct format for problem {i}")
            continue

        matches = re.findall(pattern, options[i])
        choices = [match.strip() for match in matches]

        assert len(choices) == 5, "There are not 5 options"

        a, b, c, d, e = choices

        cleaned_data.append({
            "problem" : problem[i],
            "options" : {
                "a" : a,
                "b" : b,
                "c" : c,
                "d" : d,
                "e" : e,
            },
            "gt" : correct[i],
            "type" : "arithmetic",
        })

    return cleaned_data


# The repository for math_qa contains custom code which must be executed to correctly load the dataset. 
# The repository content can be inspected at https://hf.co/datasets/math_qa.
# Need to pass the argument `trust_remote_code=True` to allow custom code to be run.

dataset = load_dataset("math_qa", trust_remote_code=True)

data = dataset["train"]
data_dict = data.to_dict()

logging.info(f"Length: {data_dict.__len__()}")
logging.info(f"Keys: {data_dict.keys()}")


cleaned_data = clean_data(data_dict)

logging.info(f"Length: {cleaned_data.__len__()}")
logging.info(f"Sample 0: {cleaned_data[0]}")


cleaned_data_path = "data/arithmetic reasoning/math_qa_processed.json"

with open(cleaned_data_path, "w") as f:
    json.dump(cleaned_data, f)

logging.info(f"Data saved at {cleaned_data_path}")

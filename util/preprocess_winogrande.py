# This file preprocesses the causal reasoning data
# Dataset source: [winogrande](https://huggingface.co/datasets/winogrande/viewer).

from datasets import load_dataset
import json
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def clean_data (data : dict) -> list:
    sentence : list = data['sentence']
    option1 : list = data['option1']
    option2 : list = data['option2']
    answer : list = data['answer']

    ans_mapping = {'1': 'a', '2': 'b'}

    assert len(sentence) == len(option1) == len(option2) == len(answer), "Lengths are not equal"

    cleaned_data = []

    for i in range(len(sentence)):
        cleaned_data.append({
            "problem" : sentence[i],
            "options" : {
                "a" : option1[i],
                "b" : option2[i],
            },
            "gt" : ans_mapping[answer[i]],
            "type" : "causal",
        })

    return cleaned_data


# The repository for winogrande contains custom code which must be executed to correctly load the dataset. 
# The repository content can be inspected at https://hf.co/datasets/winogrande.
# Need to pass the argument `trust_remote_code=True` to allow custom code to be run.

dataset = load_dataset("winogrande", "winogrande_debiased", trust_remote_code=True)

data = dataset["train"]
data_dict = data.to_dict()

logging.info(f"Length: {len(data_dict)}")
logging.info(f"Keys: {data_dict.keys()}")


cleaned_data = clean_data(data_dict)

logging.info(f"Length: {len(cleaned_data)}")
logging.info(f"Sample 0: {cleaned_data[0]}")


cleaned_data_path = "data/causal reasoning/winogrande_processed.json"

with open(cleaned_data_path, "w") as f:
    json.dump(cleaned_data, f)

logging.info(f"Data saved at {cleaned_data_path}")

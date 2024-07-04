# This file preprocesses the scientific reasoning data
# Dataset source: [SciQ](https://allenai.org/data/sciq).

import json
import logging
import random


random.seed(42)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def clean_data(data: list) -> list:
    cleaned_data = []

    for sample in data:
        choices = [
            sample["correct_answer"],
            sample["distractor1"],
            sample["distractor2"],
            sample["distractor3"],
        ]
        random.shuffle(choices)

        gt = choices.index(sample["correct_answer"])

        cleaned_data.append(
            {
                "problem": sample["question"],
                "options": {
                    "a": choices[0],
                    "b": choices[1],
                    "c": choices[2],
                    "d": choices[3],
                },
                "gt": chr(gt + 97),
                "type": "scientific",
            }
        )

    return cleaned_data


source_data_path = "data/scientific reasoning/SciQ dataset-2 3/train.json"

with open(source_data_path, "r") as f:
    source_data: list = json.load(f)

logging.info(f"Length: {len(source_data)}")
logging.info(f"Keys: {source_data[0].keys()}")


cleaned_data = clean_data(source_data)

logging.info(f"Length: {len(cleaned_data)}")
logging.info(f"Sample 0: {cleaned_data[0]}")


cleaned_data_path = "data/scientific reasoning/SciQ_processed.json"

with open(cleaned_data_path, "w") as f:
    json.dump(cleaned_data, f)

logging.info(f"Data saved at {cleaned_data_path}")

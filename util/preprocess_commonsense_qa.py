# This file preprocesses the commonsense reasoning data
# Dataset source: [CommonsenseQA](https://huggingface.co/datasets/tau/commonsense_qa/viewer).

from datasets import load_dataset
import json
import logging


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def clean_data(data: dict) -> list:
    id: list = data["id"]
    question: list = data["question"]
    question_concept: list = data["question_concept"]
    choices: list = data["choices"]
    answerKey: list = data["answerKey"]

    assert (
        len(id)
        == len(question)
        == len(question_concept)
        == len(choices)
        == len(answerKey)
    ), "Length of all the lists are not same"

    cleaned_data = []

    for i in range(len(id)):
        labels = choices[i]["label"]
        texts = choices[i]["text"]

        assert labels == ["A", "B", "C", "D", "E"], "Labels are not as expected"

        a, b, c, d, e = texts

        cleaned_data.append(
            {
                "problem": question[i],
                "options": {
                    "a": a,
                    "b": b,
                    "c": c,
                    "d": d,
                    "e": e,
                },
                "gt": answerKey[i],
                "type": "commonsense",
            }
        )

    return cleaned_data


dataset = load_dataset("tau/commonsense_qa")

data = dataset["train"]
data_dict = data.to_dict()

logging.info(f"Length: {len(data_dict)}")
logging.info(f"Sample keys: {data_dict.keys()}")


cleaned_data = clean_data(data_dict)

logging.info(f"Length: {len(cleaned_data)}")
logging.info(f"Sample 0: {cleaned_data[0]}")


cleaned_data_path = "data/commonsense reasoning/commonsense_qa_processed.json"

with open(cleaned_data_path, "w") as f:
    json.dump(cleaned_data, f)

logging.info(f"Data saved at {cleaned_data_path}")

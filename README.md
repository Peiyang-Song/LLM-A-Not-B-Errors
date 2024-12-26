# A-Not-B Errors in Pretrained Language Models

🚩**News**: [Our paper](https://arxiv.org/abs/2409.15454) is accepted to the Findings of Empirical Methods in Natural Language Processing (EMNLP) 2024. See you in Miami!

This official repository holds code for the paper "**In-Context Learning May Not Elicit Trustworthy Reasoning: A-Not-B Errors in Pretrained Language Models**". We open source all code and results here under a [permissive MIT license](LICENSE), to encourage reproduction and further research exploration.

<img width="977" alt="a-not-b-errors" src="https://github.com/user-attachments/assets/9da20cbb-c57b-4cbe-b4fb-357f72da328b">

## Repo Structure

* The [`data`](data) directory contains all processed and binarized data for the four representative reasoning tasks studied in the paper. For a detailed walkthrough, please refer to the [README](data/README.md) under that directory.

* The [`method`](method) directory contains our main code. Specifically:

1) [`A_not_B.py`](method/A_not_B.py) generates the main experiment in our paper.
2) [`A_not_B_with_explanation.py`](method/A_not_B_with_explanation.py) generates a followup experiment, investigating whether self-explanation and explicit reasoning processes can prevent LLMs from exhibiting A-Not-B errors.
3) [`A_not_B_extra_options.py`](method/A_not_B_extra_options.py) generates another followup experiment, investigating whether allowing for extra options in the MCQA problems can prevent LLMs from exhibiting A-Not-B errors.

For detailed presentations and discussions of the results, please refer to corresponding sections in our paper.

* The [`util`](util) folder contains the code that processes and binarizes data. You may reuse these scripts to process your own datasets and run A-not-B investigations on more reasoning tasks.

All code in this repository is **directly runnable** after you install the (very few) extra pip dependencies in `requirements.txt`.

## Contributions

We **welcome contributions**. Please feel free to PR to add A-not-B investigations with other LLMs or reasoning tasks. In the PR, please include a brief description and any additional information (extra setup steps required, results generated, credits to other works, etc.) you feel necessary to note. For PRs powering other potential directions of improvement, please additionally add a short explanation of the motivation behind your PR. You are also encouraged to open a discussion and chat with the maintainers of this repo before taking actions, in order to minimize opportunity costs.

## Getting in Touch

* For general questions and discussions, please use [GitHub Discussions](https://github.com/lean-dojo/LeanCopilot/discussions). 

* To report a potential bug, please open an issue. In the issue, please include the exact steps to reproduce the error, and complete logs. The more details you provide, the better we will be able to help you.

* Feature requests and other suggestions are extremely welcome. Please feel free to start a discussion!

## Code Formatting

We use [black](https://github.com/psf/black) to format code in this repository.

## Citation

If you find our work useful, please kindly cite [our paper](https://arxiv.org/abs/2409.15454).

```tex
@inproceedings{han-etal-2024-context,
    title = "In-Context Learning May Not Elicit Trustworthy Reasoning: A-Not-{B} Errors in Pretrained Language Models",
    author = "Han, Pengrui  and
      Song, Peiyang  and
      Yu, Haofei  and
      You, Jiaxuan",
    editor = "Al-Onaizan, Yaser  and
      Bansal, Mohit  and
      Chen, Yun-Nung",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2024",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.findings-emnlp.322",
    doi = "10.18653/v1/2024.findings-emnlp.322",
    pages = "5624--5643",
    abstract = "Recent advancements in artificial intelligence have led to the creation of highly capable large language models (LLMs) that can perform tasks in a human-like manner. However, LLMs exhibit only infant-level cognitive abilities in certain areas. One such area is the A-Not-B error, a phenomenon seen in infants where they repeat a previously rewarded behavior despite well-observed changed conditions. This highlights their lack of inhibitory control {--} the ability to stop a habitual or impulsive response. In our work, we design a text-based multi-choice QA scenario similar to the A-Not-B experimental settings to systematically test the inhibitory control abilities of LLMs. We found that state-of-the-art LLMs (like Llama3-8b) perform consistently well with in-context learning (ICL) but make errors and show a significant drop of as many as 83.3{\%} in reasoning tasks when the context changes trivially. This suggests that LLMs only have inhibitory control abilities on par with human infants in this regard, often failing to suppress the previously established response pattern during ICL.",
}

```

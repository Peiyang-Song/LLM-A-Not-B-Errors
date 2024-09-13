# A-Not-B Errors in Pretrained Language Models

This official repository holds code for the paper "**In-Context Learning May Not Elicit Trustworthy Reasoning: A-Not-B Errors in Pretrained Language Models**". We open source all code and results here under a [permissive MIT license](LICENSE), to encourage reproduction and further research exploration.

<img width="977" alt="a-not-b-errors" src="https://github.com/user-attachments/assets/23911dc5-f8c8-453f-b999-12b4727ab558">

## Repo Structure

* The [`data`](data) folder contains all our processed and binarized data for four representative reasoning tasks. For a detailed guide, please refer to the [README](data/README.md) under that directory.

* The [`method`](method) folder contains our main code. Specifically:

1) [`A_not_B.py`](method/A_not_B.py) generates the main experiment results in our paper.
2) [`A_not_B_with_explanation.py`](method/A_not_B_with_explanation.py) generates a followup experiment result, investigating whether self-explanation and explicit reasoning processes can prevent LLMs from exhibiting A-Not-B errors.
3) [`A_not_B_extra_options.py`](method/A_not_B_extra_options.py) generates another followup experiment result, investigating whether allowing for extra options in the MCQ problems can prevent LLMs from exhibiting A-Not-B errors.

* The [`util`](util) folder contains the code that processes and binarizes data. You may reuse these scripts to process your own datasets and run A-not-B investigations on other reasoning tasks.

All code in this repository is **directly runnable**.

## Contributions

We **welcome contributions**. Please feel free to PR to add support for more LLMs, other reasoning tasks, or more. In the PR, please include a brief description and any additional information (extra setup steps required, results generated, credits to other works, etc.) you feel necessary to note.

## Getting in Touch

* For general questions and discussions, please use [GitHub Discussions](https://github.com/lean-dojo/LeanCopilot/discussions). 

* To report a potential bug, please open an issue. In the issue, please include the exact steps to reproduce the error, and complete logs. The more details you provide, the better we will be able to help you.

* Feature requests and other suggestions are extremely welcome. Please feel free to start a discussion!

## Code Formatting

We use [black](https://github.com/psf/black) to format code in this repository.

## Citation

If you find our work useful, please kindly cite our paper.

[LINK TO BE POSTED]

# A-Not-B Errors in Pretrained Language Models

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

If you find our work useful, please kindly cite our paper.

[LINK TO BE POSTED]

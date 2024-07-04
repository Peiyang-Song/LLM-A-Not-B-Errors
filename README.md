# A-Not-B Errors in Pretrained Language Models

This official repository holds code for the paper "In-Context Learning May Not Elicit Trustworthy Reasoning: A-Not-B Errors in Pretrained Language Models". We open source all code and results here under a [permissive MIT license](LICENSE), to encourage reproduction and further research exploration.

<img width="977" alt="a-not-b-errors" src="https://github.com/Peiyang-Song/LLM-A-Not-B-Errors/assets/114432581/ae5e8f3b-4eb8-4fb3-9b9e-dbef3e6c4fb4">

## Repo Structure

The [`data`](data) folder contains all our processed and binarized data for four representative reasoning tasks. For detailed guide, please refer to the [README](data/README.md) under that directory.

The [`method`](method) folder contains our main code. Specifically:

1) [`A_not_B.py`](method/A_not_B.py) generates the main experiment in our paper.
2) [`A_not_B_with_explanation.py`](method/A_not_B_with_explanation.py) generates a followup experiment, investigating whether self-explanation and explicit reasoning can prevent LLMs from exhibiting A-Not-B errors.
3) [`A_not_B_extra_options.py`](method/A_not_B_extra_options.py) generates another followup experiment, investigating whether allowing for extra options in the MCQ problems can prevent LLMs from exhibiting A-Not-B errors.

The [`util`](util) folder contains the code that processes and binarizes data.

All code in this repository is **directly runnable**.

## Contributions

We welcome contributions. Please feel free to PR to add support for more LLMs, other reasoning tasks, or more. In the PR, please include a brief description and any additional information (more complicated setup steps, results generated, credits to other works, etc.) you feel necessary to note.

## Questions and Bugs

* For general questions and discussions, please use GitHub Discussions.

* To report a potential bug, please open an issue. In the issue, please at least include the exact steps to reproduce the error, and complete logs in debug mode. The more details you provide, the better we will be able to help you.

## Citation

If you find our work useful, please kindly cite our paper.

[TODO]

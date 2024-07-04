# Data for Representative Reasoning Tasks

## Content

In this work, we study four representative reasoning tasks, and choose one high-quality MCQ dataset for each task. The tasks and the corresponding datasets we use are

1) **Arithmetic reasoning** -- Math QA [1].
2) **Causal reasoning** -- Winogrande [2].
3) **Commonsense reasoning** -- Commonsense QA [3].
4) **Scientific reasoning** -- SciQ [4].

In this directory, each sub-folder contains our processed and binarized versions of the datasets for our investigation in this work. The processing and binarization scripts can be found under the [`util`](../util/) directory in this repo.

We exclude the original dataset from the content of this repo to better respect the original authors' great work. We however include the scripts with which we loaded the datasets in our data processing scripts. You may easily obtain the datasets using our code. The only exception is the SciQ dataset which cannot be simply loaded from HuggingFace.

## Reference

If you find our processed data useful or would like to use them in downstream research, please make sure to cite the original datasets in addition to our work. For your convenience, we provide references to the original datasets below.

[1] Math QA:

```tex
@inproceedings{amini-etal-2019-mathqa,
    title = "{M}ath{QA}: Towards Interpretable Math Word Problem Solving with Operation-Based Formalisms",
    author = "Amini, Aida  and
      Gabriel, Saadia  and
      Lin, Shanchuan  and
      Koncel-Kedziorski, Rik  and
      Choi, Yejin  and
      Hajishirzi, Hannaneh",
    editor = "Burstein, Jill  and
      Doran, Christy  and
      Solorio, Thamar",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N19-1245",
    doi = "10.18653/v1/N19-1245",
    pages = "2357--2367",
}
```

[2] Winogrande:

```tex
@article{sakaguchi2019winogrande,
    title={WinoGrande: An Adversarial Winograd Schema Challenge at Scale},
    author={Sakaguchi, Keisuke and Bras, Ronan Le and Bhagavatula, Chandra and Choi, Yejin},
    journal={arXiv preprint arXiv:1907.10641},
    year={2019}
}
```

[3] Commonsense QA:

```tex
@inproceedings{talmor-etal-2019-commonsenseqa,
    title = "{C}ommonsense{QA}: A Question Answering Challenge Targeting Commonsense Knowledge",
    author = "Talmor, Alon  and
      Herzig, Jonathan  and
      Lourie, Nicholas  and
      Berant, Jonathan",
    editor = "Burstein, Jill  and
      Doran, Christy  and
      Solorio, Thamar",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N19-1421",
    doi = "10.18653/v1/N19-1421",
    pages = "4149--4158",
}
```

[4] SciQ:

```tex
@inproceedings{welbl-etal-2017-crowdsourcing,
    title = "Crowdsourcing Multiple Choice Science Questions",
    author = "Welbl, Johannes  and
      Liu, Nelson F.  and
      Gardner, Matt",
    editor = "Derczynski, Leon  and
      Xu, Wei  and
      Ritter, Alan  and
      Baldwin, Tim",
    booktitle = "Proceedings of the 3rd Workshop on Noisy User-generated Text",
    month = sep,
    year = "2017",
    address = "Copenhagen, Denmark",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W17-4413",
    doi = "10.18653/v1/W17-4413",
    pages = "94--106",
}
```
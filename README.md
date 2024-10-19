# NormTab: Improving Symbolic Reasoning in LLMs Through Tabular Data Normalization [EMNLP 2024]

## Method Overview 

<image src="/NormTab.jpg"/>


## Abstract
In recent years, Large Language Models (LLMs) have demonstrated remarkable capabilities in parsing textual data and generating code. However, their performance in tasks involving tabular data, especially those requiring
symbolic reasoning, faces challenges due to the structural variance and inconsistency in table cell values often found in web tables. In this paper, we introduce NormTab, a novel framework aimed at enhancing the symbolic
reasoning performance of LLMs by normalizing web tables. We study table normalization as a stand-alone, one-time preprocessing step using LLMs to support symbolic reasoning on tabular data. Our experimental evaluation, conducted on challenging web table datasets such as WikiTableQuestion and TabFact, demonstrates that leveraging NormTab significantly improves symbolic reasoning performance, showcasing the importance and effectiveness of web table normalization for enhancing LLM-based symbolic reasoning tasks.


## Code 

Install requirements 

> for wikitq: run_normtab_wtq.py

> for tf: run_normtab_tf.py

> for eval wikitq: normtab_wtq_eval.py

> for eval tf: normtab_tf_eval.py

## Citation

If you want to cite our papers, please use:

```bibtex
@inproceedings{
nahid2024normtab,
title={NormTab: Improving Symbolic Reasoning in {LLM}s Through Tabular Data Normalization},
author={Md Mahadi Hasan Nahid and Davood Rafiei},
booktitle={The 2024 Conference on Empirical Methods in Natural Language Processing},
year={2024},
url={https://openreview.net/forum?id=qwWTmgorEL}
}
```

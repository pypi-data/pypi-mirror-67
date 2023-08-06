# Efficient First Stage Retrieval using Dense Representations and KNN
> Summary description here.


This file will become your README and also the index of your documentation.

## Install

`pip install efficient_first_stage_retrieval`

## How to use

Use calculate_score to calculate MAP and MRR from actual qrels in fn_qrels and from predictions in prediction

```python
calculate_score(fn_qrels='data/robust/qrels.robust2004.txt', prediction="score.txt")
```

Use do_run to calculate predictions from 'searcher' and queries 'topic' and used time and store it in file and 'time-' + file

```python
do_run(file, topics, searcher)
```

# BERT Product Rating Predictor

## Overview

* **Year:** 2020
* **Language(s):** Python, R
* **Discipline(s):** Machine Learning, Natural Language Processing (NLP)
* **Keywords:** `Amazon Reviews`, `BERT`, `Classification`, `Clustering`, `Machine Learning`, `NLP`

## Description

The *BERT Product Rating Predictor* is a natural language processing model based on the *Bidirectional Encoder Representations from Transformers (BERT)* model developed to predict star ratings for textual product reviews. It was created by fine-tuning the BERT model, training it with a custom dataset containing 195,765 reviews gathered from Amazon’s electronic products section. From this model, a $k$-means clustering model was then employed to explore interesting relationships between the predicted star ratings and their associated reviews.

This model was then used as part of a research project titled *Using the BERT Model to Predict and Analyze Product Ratings Based on Reviews*.

## Build Instructions

1. Download the `bert-product-rating-predictor.ipynb` Jupyter notebook.
2. Download the [pretrained model](https://bit.ly/2VENkSB).
3. In the notebook, set up the pretrained model by adding the pretrained model to the same directory and including it as the `file_path`. More instructions can be found in the notebook.
4. Reach the end of the notebook and define a custom `review`.
5. Run the notebook. The last block will contain your predicted star rating.

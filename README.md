# Unsupervised-Clustering-Solutions

This repository contains a Python project that performs unsupervised clustering using the KMeans algorithm on a dataset of mall customers. The project includes data loading, model training, and evaluation scripts.

## Installation
1. Clone the repository:
   '''sh
   git clone https://github.com/kaurrmanpreett/Unsupervised-Clustering-Solutions.git

2. Create a virtual environment (optional but recommended):
   '''sh
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Install the required packages:
   '''sh
   pip install -r requirements.txt

## Usage
1. Ensure that the mall_customers.csv file is located in the data/ directory.

2. Run the main.py script to load the data, train the KMeans models, and evaluate the clustering solutions:
   python main.py

## Project Modules
1. imports.py: Contains the necessary imports and suppresses warnings.

2. data_loading.py: Functions for loading and checking the data.

3. model_training.py: Functions for training KMeans models with different feature sets and evaluating them using the elbow and silhouette methods.

4. model_evaluation.py: Functions for visualizing the clustering results.

## License
This project is licensed under the Apache License 2.0.

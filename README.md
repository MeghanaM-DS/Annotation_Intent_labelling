# Annotation_Intent_labelling

Name: Meghana Maringanti

Course: INFO 555 - Applied NLP - University of Arizona

This repository contains the necessary files, scripts, and data for the annotation and validation of labeled queries, along with a quality-check process. The repository is structured to handle data labeling, merging annotations, resolving disagreements, and validating the annotations using a model. 

---

## Repository Structure

Write-up
│
└── Contains the paper write-up.
├── data/
│   ├── queries.txt              # Text file with raw queries.
│   ├── queries.csv              # CSV file with structured queries.
│   └── final_dataset.csv        # Generated dataset for further analysis.
├── Labelling/
│   ├── Annotator_1.csv          # Labels provided by Annotator 1.
│   ├── Annotator_2.csv          # Labels provided by Annotator 2.
│   ├── disagreements.csv        # Queries with conflicting labels from annotators.
│   └── combined_labels.csv      # Merged labels from both annotators.
├── images/
│   └── Visualizations used in the write-up.
├── requirements.txt             # Python package dependencies.
├── Annotation Guidelines.txt    # Guidelines for annotation.
├── Datasets.py                  # Script to merge annotations and resolve disagreements.
├── queries.py                   # Script to write queries from text to CSV.
├── quality_check.py             # Script to check data quality using Cohen's Kappa.
└── Annotation_validation.ipynb  # Notebook for model-based validation.



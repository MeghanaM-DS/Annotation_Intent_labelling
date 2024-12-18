# Annotation_Intent_labelling

Name: Meghana Maringanti

Course: INFO 555 - Applied NLP - University of Arizona

This repository contains the necessary files, scripts, and data for the annotation and validation of labeled queries, along with a quality-check process. The repository is structured to handle data labeling, merging annotations, resolving disagreements, and validating the annotations using a model. 

---

## Repository Structure

## Write-up
Contains the paper write-up.

### Directories and Files
- **data/**  
  - `queries.txt` - Text file with raw queries.  
  - `queries.csv` - CSV file with structured queries.  
  - `final_dataset.csv` - Generated dataset for further analysis.
  - `Predicted_labels.csv` - Predicted labels  using model.
  - `classification_report.csv` - Metrics used to measure performance for each label.
  - `per_label_scores.csv` - Precison, Recall, F1-scores for each label.

- **Labelling/**  
  - `Annotator_1.csv` - Labels provided by Annotator 1.  
  - `Annotator_2.csv` - Labels provided by Annotator 2.  
  - `disagreements.csv` - Queries with conflicting labels from annotators.  
  - `combined_labels.csv` - Merged labels from both annotators.  

- **images/**  
  - Contains visualizations used in the write-up.  

### Additional Files
- `requirements.txt` - Python package dependencies.  
- `Annotation Guidelines.txt` - Guidelines for annotation.  
- `Datasets.py` - Script to merge annotations and get disagreements.  
- `queries.py` - Script to write queries from text to CSV file.  
- `quality_check.py` - Script to check data quality using Cohen's Kappa.  
- `Annotation_validation.ipynb` - Notebook for model-based validation.



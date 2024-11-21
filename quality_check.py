"""
quality_check.py

This script evaluates the quality of annotations by calculating inter-annotator agreement using Cohen's Kappa.

"""
import pandas as pd
from collections import Counter
merged_df = pd.read_csv('Labelling/combined_labels.csv')

# Step1: Get Agreement/disagreement values
merged_df['agreement'] = merged_df['label_1'] == merged_df['label_2']
total_instances = len(merged_df)
agreements = merged_df['agreement'].sum()
disagreements = total_instances - agreements

print(f"Total Instances: {total_instances}")
print(f"Agreements: {agreements}")
print(f"Disagreements: {disagreements}")

# Calculate observed agreement (P_o)
P_o = agreements / total_instances
print(f"\nObserved Agreement (P_o): {P_o:.3f}")

# Step 2: Calculate proportions for each label
label_counts_1 = Counter(merged_df['label_1'])
label_counts_2 = Counter(merged_df['label_2'])

proportions_1 = {}
proportions_2 = {}


for label, count in label_counts_1.items():
    proportion = count / total_instances
    proportions_1[label] = proportion


for label, count in label_counts_2.items():
    proportion = count / total_instances
    proportions_2[label] = proportion

print("Proportions for Annotator 1:", proportions_1)

print("Proportions for Annotator 2:", proportions_2)


all_labels = set(proportions_1.keys()).union(proportions_2.keys())
P_e = 0
for label in all_labels:
    p1 = proportions_1.get(label, 0)  # default 0 if not found
    p2 = proportions_2.get(label, 0)
    P_e += p1 * p2  # Sum the products for each label

print(f"\nChance Agreement (P_e): {P_e:.3f}")

# Step 4: Calculate Cohen's Kappa
if P_e != 1:  # To avoid division by zero in rare cases
    kappa = (P_o - P_e) / (1 - P_e)
else:
    kappa = 0

print(f"\nCohen's Kappa: {kappa:.3f}")

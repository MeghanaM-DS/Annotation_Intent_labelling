import pandas as pd

df1 = pd.read_csv('Labelling/Annotator1_labels.csv')
df2 = pd.read_csv('Labelling/Annotator2_labels.csv')
print(df1.columns)
print(df2.columns)
merged_df = pd.merge(df1, df2, on=['Query_Id', 'query'], suffixes=('_1', '_2'))
merged_df = merged_df[['Query_Id', 'query', 'label_1', 'label_2']]
merged_df.to_csv('Labelling/combined_labels.csv', index=False)

label_counts_1 = merged_df['label_1'].value_counts()
print("Label counts for Annotator 1:")
print(label_counts_1)

label_counts_2 = merged_df['label_2'].value_counts()
print("\nLabel counts for Annotator 2:")
print(label_counts_2)

disagreements = merged_df[merged_df['label_1'] != merged_df['label_2']]
disagreements.to_csv("Labelling\disagreements.csv", index=False)

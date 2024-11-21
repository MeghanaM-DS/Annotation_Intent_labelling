"""
queries.py

This script converts raw queries from a text file (`queries.txt`) into a structured CSV format (`queries.csv`).

"""
import pandas as pd
import re

with open("data/queries.txt", 'r') as file:
    lines = file.readlines()


# Extract content inside double quotes
def extract_query(line):
    """
    This is function is used to extract query from each line.
    :param line: line from the text file
    :return: content if pattern matches, None is not
    """
    match = re.search(r'"([^"]*)"', line)
    if match:
        return match.group(1)
    return None


data = [extract_query(line) for line in lines if extract_query(line)]

# Convert to DataFrame
df = pd.DataFrame(data, columns=["query"])
file_name = "data/queries.csv"
df.to_csv(file_name, index=False)

print("Queries have been written to excel_file")

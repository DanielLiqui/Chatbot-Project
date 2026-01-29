import os
import pandas as pd
import sys


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
CSV_INPUT = os.path.join(BASE_DIR, 'dataset.csv')
CSV_OUTPUT = os.path.join(BASE_DIR, 'dataset_clean.csv')


try:
    df = pd.read_csv(CSV_INPUT)
except FileNotFoundError:
    print(f"Error: file {CSV_INPUT} not found!")
    sys.exit(1)

print(f"Original dataset downloaded, size: {df.shape}")


if not all(col in df.columns for col in ['utterance', 'category', 'intent']):
    print("Error: CSV must have columns 'utterance', 'category', 'intent'")
    sys.exit(1)

df_clean = df[['utterance', 'category', 'intent']].copy()
df_clean.rename(columns={'utterance': 'text'}, inplace=True)


df_clean = df_clean.dropna(subset=['text', 'intent'])

df_clean = df_clean.drop_duplicates(subset=['text'])

df_clean = df_clean[df_clean['text'].str.len() > 5]

df_clean.to_csv(CSV_OUTPUT, index=False)
print(f"Clean dataset saved: {CSV_OUTPUT}, size: {df_clean.shape}")
print("\nExamples strings after cleaning:\n", df_clean.head())

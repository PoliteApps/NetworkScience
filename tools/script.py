import pandas as pd

# Function to process the JSONL data
def process_jsonl_to_dataframe(jsonl_file):
    # Load the JSONL data into a pandas DataFrame
    df = pd.read_json(jsonl_file, lines=True)

    # Keep only the relevant columns
    df = df[['id', 'question', 'alternatives', 'label', 'figures']]

    # Transform the 'figures' column to 'has_figure'
    df['has_figure'] = df['figures'].apply(lambda x: len(x) > 0)

    # Drop the 'figures' column
    df = df.drop(columns=['figures'])

    return df

# Example usage
jsonl_file = 'datasets/2023.jsonl'  # Replace with your actual file path
df = process_jsonl_to_dataframe(jsonl_file)
df.to_csv("datasets/questions_2023.csv")

jsonl_file = 'datasets/2022.jsonl'  # Replace with your actual file path
df = process_jsonl_to_dataframe(jsonl_file)
df.to_csv("datasets/questions_2022.csv")

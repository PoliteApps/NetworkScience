import pandas as pd

# Load the ENEM dataset
df = pd.read_csv('datasets/microdados_enem_2022/DADOS/MICRODADOS_ENEM_2022.csv', encoding='ISO-8859-1')  # Replace with the actual path to your ENEM dataset

# Define the sample size (e.g., 5000)
sample_size = 5000

# Randomly sample the dataset
df_sample = df.sample(n=sample_size, random_state=42)

# Save the sample to a new CSV file
df_sample.to_csv('enem_random_sample.csv', index=False)

print(f"Random sample saved to 'enem_random_sample.csv'.")
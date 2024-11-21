import pandas as pd

# Load the dataset (adjust the path to your actual file)
df = pd.read_csv('enem_random_sample.csv', encoding='ISO-8859-1', sep=';')

# List of columns for the first dataset (NU_INSCRICAO + TX_RESPOSTAS_)
columns_first_dataset = ['NU_INSCRICAO', 'TX_RESPOSTAS_CN', 'TX_RESPOSTAS_CH', 'TX_RESPOSTAS_LC', 'TX_RESPOSTAS_MT']

# Create the first dataset by selecting the relevant columns
df_first = df[columns_first_dataset]

# Create the second dataset by selecting NU_INSCRICAO and the rest of the columns
df_second = df.drop(columns=columns_first_dataset)

# Save both datasets to separate CSV files
df_first.to_csv('enem_responses_dataset.csv', index=False)
df_second.to_csv('enem_dif_dataset.csv', index=False)

print(f"First dataset saved to 'enem_first_dataset.csv'.")
print(f"Second dataset saved to 'enem_second_dataset.csv'.")

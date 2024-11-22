import pandas as pd

# Load the dataset (adjust the path to your actual file)
df = pd.read_csv('../temp_data/enem_random_sample.csv', encoding='ISO-8859-1', sep=',')

# List of columns for the first dataset (NU_INSCRICAO + TX_RESPOSTAS_)
columns_first_dataset = ['NU_INSCRICAO', 'TX_RESPOSTAS_CN', 'TX_RESPOSTAS_CH', 'TX_RESPOSTAS_LC', 'TX_RESPOSTAS_MT']

# Create the first dataset by selecting the relevant columns
df_first = df[columns_first_dataset]

# Create the second dataset by selecting NU_INSCRICAO and the rest of the columns
df_second = df.drop(columns=columns_first_dataset)

# Save both datasets to separate CSV files
df_second.to_csv('enem_dif_dataset.csv', index=False)

# Generate *.csv with answers

# CN TEST
df = df_first[['NU_INSCRICAO','TX_RESPOSTAS_CN']]
df_answers = df['TX_RESPOSTAS_CN'].str.split('', n=45, expand=True)
df_answers = df_answers.iloc[: , 1:]
df = pd.concat([df['NU_INSCRICAO'], df_answers], axis=1)
df.rename(columns={'NU_INSCRICAO':"question_number"}, inplace=True)
df.to_csv('enem_responses_CN_dataset.csv', index=False)

# CH TEST
df = df_first[['NU_INSCRICAO','TX_RESPOSTAS_CH']]
df_answers = df['TX_RESPOSTAS_CH'].str.split('', n=45, expand=True)
df_answers = df_answers.iloc[: , 1:]
df = pd.concat([df['NU_INSCRICAO'], df_answers], axis=1)
df.rename(columns={'NU_INSCRICAO':"question_number"}, inplace=True)
df.to_csv('enem_responses_CH_dataset.csv', index=False)

# LC TEST
df = df_first[['NU_INSCRICAO','TX_RESPOSTAS_LC']]
df_answers = df['TX_RESPOSTAS_LC'].str.split('', n=45, expand=True)
df_answers = df_answers.iloc[: , 1:]
df = pd.concat([df['NU_INSCRICAO'], df_answers], axis=1)
df.rename(columns={'NU_INSCRICAO':"question_number"}, inplace=True)
df.to_csv('enem_responses_LC_dataset.csv', index=False)

# MT TEST
df = df_first[['NU_INSCRICAO','TX_RESPOSTAS_MT']]
df_answers = df['TX_RESPOSTAS_MT'].str.split('', n=45, expand=True)
df_answers = df_answers.iloc[: , 1:]
df = pd.concat([df['NU_INSCRICAO'], df_answers], axis=1)
df.rename(columns={'NU_INSCRICAO':"question_number"}, inplace=True)
df.to_csv('enem_responses_MT_dataset.csv', index=False)

print(f"First dataset saved to 'enem_first_dataset.csv'.")


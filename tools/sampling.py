import pandas as pd

from tqdm import tqdm

# Helper function to load datasets which are too big
def load_huge_csv(filename):
    # the number of row in each data frame
    # you can put any value here according to your situation
    chunksize = 1000

    # the list that contains all the dataframes
    list_of_dataframes = []    

    for df in tqdm(pd.read_csv(filename, chunksize=chunksize, encoding="ISO-8859-1", sep=";")):
        # process your data frame here
        # then add the current data frame into the list
        list_of_dataframes.append(df)

    # if you want all the dataframes together, here it is
    return pd.concat(list_of_dataframes)

# Load the ENEM dataset
print('Loading data...')
df = load_huge_csv("../datasets/2022/DADOS/MICRODADOS_ENEM_2022.csv")  # Replace with the actual path to your ENEM dataset

# Filter to use only data which matchs Maritaca database
print('Filtering data...')
df_filtred = df[(df['CO_PROVA_CN'] == 1087) & 
                (df['CO_PROVA_CH'] == 1057) & 
                (df['CO_PROVA_LC'] == 1068) & 
                (df['CO_PROVA_MT'] == 1078)]

# Define the sample size (e.g., 5000)
sample_size = 5000

# Randomly sample the dataset
print('Sampling...')
df_sample = df_filtred.sample(n=sample_size, random_state=42)

# Save the sample to a new CSV file
print('Saving *.csv...')
df_sample.to_csv('enem_random_sample.csv', index=False)

print(f"Random sample saved to 'enem_random_sample.csv'.")
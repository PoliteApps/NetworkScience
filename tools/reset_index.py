import pandas as pd

# Load your dataset
data = pd.read_csv('treated_data/questions_part4.csv')

# Drop the current index column (Unnamed: 0) and reset the index
data = data.drop(columns=['Unnamed: 0']).reset_index(drop=True)

# Save the updated dataset back to a CSV if needed
data.to_csv('treated_data/questions_part4.csv', index=False)

# Display the updated dataset
print(data)

import pandas as pd

for i in range(4):
    addition = i*45
    df = pd.read_csv(f"scores/scores-p{i+1}.csv",index_col=0)
    # Step 1: Drop the 'statement' column
    df.drop(columns=['Score'], inplace=True)
    df.columns = [
    str(int(col) + addition) if idx >= 1 and col.isdigit() else col
    for idx, col in enumerate(df.columns)
    ]
    df.to_csv(f'scores/student_question_matrix{i+1}.csv')

import pandas as pd

def get_label_row(csv_file):
    """
    Reads the questions.csv file and extracts the label column.
    Returns a list starting with 'true_answers' followed by the labels.
    """
    df = pd.read_csv(csv_file)
    label_row = ["true_answers"] + df['label'].tolist()
    return label_row


def transform_data(csv_file):
    """
    Transforms the questions.csv data into the desired format.
    Parses the 'alternatives' column to create option_1, option_2, etc.
    Returns a DataFrame with the new structure.
    """
    df = pd.read_csv(csv_file)

    # Parse the alternatives string and split into separate columns
    transformed_data = {
        "question_number": df['id'],
        "statement": df['question'],
        "option_1": df['alternatives'].apply(lambda x: eval(x)[0] if isinstance(eval(x), list) and len(eval(x)) > 0 else ""),
        "option_2": df['alternatives'].apply(lambda x: eval(x)[1] if isinstance(eval(x), list) and len(eval(x)) > 1 else ""),
        "option_3": df['alternatives'].apply(lambda x: eval(x)[2] if isinstance(eval(x), list) and len(eval(x)) > 2 else ""),
        "option_4": df['alternatives'].apply(lambda x: eval(x)[3] if isinstance(eval(x), list) and len(eval(x)) > 3 else ""),
    }
    return pd.DataFrame(transformed_data)

def adjust_question_numbers(df):
    """
    Adjusts the question_number column to be index + 1.
    Modifies the DataFrame in place and returns it.
    """
    df['question_number'] = df.index + 1
    return df

def process_exam_file(exam_path, output_path, start_id, end_id, label_row):
    """
    Processes an exam file:
    1. Updates the first row to the appropriate range of question IDs (start_id to end_id).
    2. Adds the label row as the second row.
    3. Saves the modified exam to a new file.
    
    Parameters:
        exam_path (str): Path to the original exam CSV file.
        output_path (str): Path to save the processed exam CSV file.
        start_id (int): Start of the question ID range.
        end_id (int): End of the question ID range.
        label_row (list): The label row starting with "true_answers".
    """
    # Load the exam data
    exam_df = pd.read_csv(exam_path, header=None)  # Assuming no header row
    
    # Create the new first row with the appropriate range
    question_ids = list(range(start_id, end_id + 1))
    question_ids.insert(0, "question_number")
    
    # Adjust the question_ids list to match the number of columns
    if len(question_ids) < exam_df.shape[1]:
        # Pad with empty strings if too short
        question_ids += [""] * (exam_df.shape[1] - len(question_ids))
    elif len(question_ids) > exam_df.shape[1]:
        # Truncate if too long
        question_ids = question_ids[:exam_df.shape[1]]
    
    # Update the first row with the adjusted question IDs
    exam_df.iloc[0] = question_ids
    
    # Extract the relevant labels for this range
    labels_for_range = ["true_answers"] + label_row[start_id:end_id + 1]
    
    # Adjust the labels_for_range list to match the number of columns
    if len(labels_for_range) < exam_df.shape[1]:
        # Pad with empty strings if too short
        labels_for_range += [""] * (exam_df.shape[1] - len(labels_for_range))
    elif len(labels_for_range) > exam_df.shape[1]:
        # Truncate if too long
        labels_for_range = labels_for_range[:exam_df.shape[1]]
    
    # Insert the label row as the second row
    label_df = pd.DataFrame([labels_for_range])
    exam_df = pd.concat([exam_df.iloc[:1], label_df, exam_df.iloc[1:]], ignore_index=True)
    
    # Save the modified DataFrame to a new file
    exam_df.to_csv(output_path, index=False, header=False)




transformed_df = transform_data("treated_data/questions_2022.csv")
treated_questions = adjust_question_numbers(transformed_df)
treated_questions.to_csv("treated_data/questions_2022_formatted.csv")

exam1 = "temp_data/enem_responses_LC_dataset.csv"
exam2 = "temp_data/enem_responses_CH_dataset.csv"
exam3 = "temp_data/enem_responses_CN_dataset.csv"
exam4 = "temp_data/enem_responses_MT_dataset.csv"

# Paths to the exams
exam_paths = [exam1, exam2, exam3, exam4]
output_paths = ["treated_data/processed_exam1.csv", "treated_data/processed_exam2.csv", "treated_data/processed_exam3.csv", "treated_data/processed_exam4.csv"]

# Define the question ID ranges for each exam
id_ranges = [(1, 45), (46, 90), (91, 135), (136, 180)]

label_row = get_label_row("treated_data/questions_2022.csv")

# Process each exam
for exam_path, output_path, (start_id, end_id) in zip(exam_paths, output_paths, id_ranges):
    process_exam_file(exam_path, output_path, start_id, end_id, label_row)

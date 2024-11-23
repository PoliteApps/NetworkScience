import pandas as pd

def process_dif_file(exam_path, dif_path, output_path):
    """
    Processes exam and dif files to create a new dataset containing student IDs and selected columns.
    
    Parameters:
        exam_path (str): Path to the `exam.csv` file.
        dif_path (str): Path to the `dif.csv` file.
        output_path (str): Path to save the processed file.
    """
    # Step 1: Load `exam.csv` and extract student IDs
    exam_df = pd.read_csv(exam_path)
    student_ids = exam_df["NU_INSCRICAO"]

    # Step 2: Load `dif.csv` and select the specified columns
    dif_df = pd.read_csv(dif_path)
    selected_columns = ["TP_SEXO", "TP_COR_RACA", "IN_TREINEIRO", "TP_ESCOLA"]
    if not set(selected_columns).issubset(dif_df.columns):
        raise ValueError(f"The columns {selected_columns} are not all present in {dif_path}")
    
    dif_selected = dif_df[selected_columns]

    # Step 3: Add student IDs as the first column
    # output_df = pd.DataFrame(student_ids, columns=["Student_ID"])
    output_df = pd.concat([student_ids, dif_selected.reset_index(drop=True)], axis=1)

    # Step 4: Save the result to a new file
    output_df.to_csv(output_path, index=False)

# File paths
exam_path = "temp_data/enem_random_sample.csv"
dif_path = "temp_data/enem_dif_dataset.csv"
output_path = "treated_data/processed_dif.csv"

# Process and save the new file
process_dif_file(exam_path, dif_path, output_path)

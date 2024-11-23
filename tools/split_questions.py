import pandas as pd

def split_questions_by_range(input_path, output_dir):
    """
    Splits the `questions_formatted.csv` file into four separate CSVs based on question ranges.
    
    Parameters:
        input_path (str): Path to the `questions_formatted.csv` file.
        output_dir (str): Directory where the split files will be saved.
    """
    # Load the CSV
    questions_df = pd.read_csv(input_path)
    
    # Define the ranges and corresponding output file names
    ranges = [(1, 45), (46, 90), (91, 135), (136, 180)]
    output_files = [
        f"{output_dir}/questions_part1.csv",
        f"{output_dir}/questions_part2.csv",
        f"{output_dir}/questions_part3.csv",
        f"{output_dir}/questions_part4.csv"
    ]
    
    # Split and save each range
    for (start, end), output_file in zip(ranges, output_files):
        # Filter rows within the range
        subset_df = questions_df[(questions_df["question_number"] >= start) & (questions_df["question_number"] <= end)]
        
        # Save the subset to a new file
        subset_df.to_csv(output_file, index=False)

        print(f"Saved questions from {start} to {end} to {output_file}")

input_path = "treated_data/questions_2022_formatted.csv"
output_dir = "treated_data"  # Directory where the split files will be saved
split_questions_by_range(input_path, output_dir)
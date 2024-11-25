import pandas as pd

for i in range(4):
    df = pd.read_csv(f"maps/map{i+1}.csv")

    # Step 1: Drop the 'statement' column
    df = df.drop(columns=['statement'])

    # Step 2: Convert 'mapped_topics' from string to list
    df['mapped_topics'] = (
        df['mapped_topics']
        .str.replace('.', '')  # Remove dots
        .str.replace('\n', '', regex=False)  # Remove newlines
        .str.replace(',', ';')               # Replace commas with semicolons
        .apply(lambda x: x.split(';'))       # Split on semicolons
    )    
    unique_topics = sorted(set(topic for topics in df['mapped_topics'] for topic in topics))

    # Step 4: Create a new dataset with questions and topics
    def create_topic_matrix(df, unique_topics):
        topic_matrix = pd.DataFrame(0, index=df['question_number'], columns=unique_topics)
        
        for _, row in df.iterrows():
            for topic in row['mapped_topics']:
                topic_matrix.loc[row['question_number'], topic] = 1
        
        return topic_matrix

    # Create the topic matrix
    topic_matrix = create_topic_matrix(df, unique_topics)

    # Display the resulting dataset
    print(topic_matrix)

    # Optionally save to CSV
    topic_matrix.to_csv(f'maps/question_topic_matrix{i+1}.csv', index=True)

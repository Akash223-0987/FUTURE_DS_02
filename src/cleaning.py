import pandas as pd
import os

def clean_data(input_path, output_path):
    print(f"Loading raw data from {input_path}...")
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return False
        
    df = pd.read_csv(input_path)   
    df['Churn'] = df['EngagementLevel'].apply(lambda x: 1 if x == 'Low' else 0)
    
    churn_rate = df['Churn'].mean() * 100
    print(f"Data Processed. Churn Rate: {round(churn_rate, 2)}%")
    
    df.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved to {output_path}")
    return True

if __name__ == "__main__":
    clean_data("data/online_gaming_behavior_dataset.csv", "data/gaming_behavior_cleaned.csv")

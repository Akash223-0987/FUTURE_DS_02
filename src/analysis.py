import pandas as pd
import os

def run_analysis(data_path):
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found.")
        return
        
    df = pd.read_csv(data_path) 

    print("--- Dataset Summary ---")
    print(f"Total Records: {len(df)}")
    
    print("\n--- Engagement vs Churn ---")
    print(pd.crosstab(df['EngagementLevel'], df['Churn']))
    
    print("\n--- Average Metrics by Churn ---")
    
    metrics = ["SessionsPerWeek", "AvgSessionDurationMinutes", "PlayerLevel"]
    analysis_results = df.groupby("Churn")[metrics].mean()
    print(analysis_results)
    
    return analysis_results

if __name__ == "__main__":
    cleaned_data_path = "data/gaming_behavior_cleaned.csv"
    run_analysis(cleaned_data_path)

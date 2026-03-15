import os
from src.cleaning import clean_data
from src.analysis import run_analysis
from src.visualization import create_visualizations

def main():
    print("=== Gaming Behavior Analysis Pipeline ===")
    
    raw_data = "data/online_gaming_behavior_dataset.csv"
    cleaned_data = "data/gaming_behavior_cleaned.csv"
    
    # 1. Cleaning
    print("\n--- Step 1: Data Cleaning ---")
    if not clean_data(raw_data, cleaned_data):
        print("Pipeline failed at Step 1.")
        return

    # 2. Analysis
    print("\n--- Step 2: Running Analysis ---")
    run_analysis(cleaned_data)

    # 3. Visualizations
    print("\n--- Step 3: Generating Visualizations ---")
    create_visualizations(cleaned_data)

    print("\n=== Pipeline Completed Successfully ===")

if __name__ == "__main__":
    main()


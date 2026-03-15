import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="whitegrid", palette="muted")

def create_visualizations(data_path, output_dir="images"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print(f"Loading data from {data_path}...")
    df = pd.read_csv(data_path)
    
    # 1. Churn Distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Churn', data=df)
    plt.title('Distribution of Churn')
    plt.xlabel('Churn (0 = No, 1 = Yes)')
    plt.ylabel('Count')
    plt.savefig(f"{output_dir}/churn_distribution.png")
    plt.close()
    
    # 2. Engagement Level vs Churn
    plt.figure(figsize=(10, 6))
    sns.countplot(x='EngagementLevel', hue='Churn', data=df)
    plt.title('Engagement Level vs Churn')
    plt.savefig(f"{output_dir}/engagement_vs_churn.png")
    plt.close()
    
    # 3. Average Session Duration by Churn (Boxplot)
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Churn', y='AvgSessionDurationMinutes', data=df)
    plt.title('Average Session Duration by Churn')
    plt.savefig(f"{output_dir}/session_duration_boxplot.png")
    plt.close()

    # 4. Correlation Heatmap (numeric columns only)
    plt.figure(figsize=(12, 10))
    numeric_df = df.select_dtypes(include=['number'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/correlation_heatmap.png")
    plt.close()

    print(f"All visualizations saved to {output_dir}/ directory.")

if __name__ == "__main__":
    cleaned_data_path = "data/gaming_behavior_cleaned.csv"
    if os.path.exists(cleaned_data_path):
        create_visualizations(cleaned_data_path)
    else:
        print("Cleaned data not found. Please run cleaning.py first.")

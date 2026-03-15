import sys
import os

# Add root to path so we can import src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.cleaning import clean_data

if __name__ == "__main__":
    clean_data("data/online_gaming_behavior_dataset.csv", "data/gaming_behavior_cleaned.csv")

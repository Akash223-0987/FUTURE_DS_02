# Gaming Behavior Analysis Project

This project analyzes online gaming behavior to identify patterns related to player churn.

## Project Structure
- `data/`: Contains raw and cleaned datasets.
- `src/`: Core logic modules.
  - `cleaning.py`: Data preprocessing and feature engineering (Churn column).
  - `analysis.py`: Descriptive statistics and churn analysis.
  - `visualization.py`: Generates charts and saved them to `images/`.
- `images/`: Output directory for generated visualizations.
- `requirements.txt`: Project dependencies.
- `main.py`: Main entry point to run the full pipeline.

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the full pipeline:
   ```bash
   python main.py
   ```

## Key Findings
- **Churn Definition**: Players with a 'Low' EngagementLevel are categorized as Churned.
- **Visualizations**: Check the `images/` directory for churn distribution, engagement comparisons, and session duration analysis.

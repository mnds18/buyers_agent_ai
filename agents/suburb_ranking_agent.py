# agents/suburb_ranking_agent.py

import pandas as pd
import os

DSR_FILE_PATH = os.path.join("data", "dummy_suburb_scores.csv")

def load_suburb_data():
    df = pd.read_csv(DSR_FILE_PATH)
    return df

def recommend_suburbs(goal="high_growth", top_n=5):
    df = load_suburb_data()

    if goal == "high_growth":
        # Rank by Growth Potential then DSR Score
        df = df.sort_values(by=["Growth_Potential_Percentage", "DSR_Score"], ascending=False)
    elif goal == "high_yield":
        # Rank by Yield % then DSR Score
        df = df.sort_values(by=["Yield_Percentage", "DSR_Score"], ascending=False)
    else:
        df = df.sort_values(by="DSR_Score", ascending=False)

    return df.head(top_n).to_dict(orient="records")

if __name__ == "__main__":
    print(recommend_suburbs(goal="high_growth"))

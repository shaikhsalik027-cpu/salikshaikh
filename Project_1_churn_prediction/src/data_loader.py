import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load churn dataset."""
    return pd.read_csv(path)

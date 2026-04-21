import pandas as pd

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=["customerID"])

    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    categorical_cols = df.select_dtypes(include="object").columns

    df = pd.get_dummies(
        df, columns=categorical_cols, drop_first=True, sparse=True
    )

    return df

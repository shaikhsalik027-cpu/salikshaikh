from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def train_logistic_regression(X, y):
    model = LogisticRegression(
        solver="liblinear", max_iter=1000
    )
    model.fit(X, y)
    return model

def train_random_forest(X, y):
    model = RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        class_weight="balanced",
        n_jobs=-1
    )
    model.fit(X, y)
    return model

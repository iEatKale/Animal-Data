import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from src.machine_learning.ml_preprocessing import build_preprocessor


def prep_classification_data(df):
    """
    Prepares features and target for animal_type classification.
    """

    target_column = "animal_type"

    feature_columns = [
        "country",
        "weight_kg",
        "body_length_cm",
        "gender",
        "latitude",
        "longitude"
    ]

    x = df[feature_columns]
    y = df[target_column]

    return x, y


def build_classification_pipeline():
    """
    Builds a machine learning pipeline for animal_type classification.
    """

    categorical_features = ["country", "gender"]

    numerical_features = [
        "weight_kg",
        "body_length_cm",
        "latitude",
        "longitude"
    ]

    preprocessor = build_preprocessor(
        categorical_features,
        numerical_features
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    return pipeline


def train_classification_model(df):
    """
    Trains and evaluates a Random Forest classifier for predicting animal_type.
    """

    x, y = prep_classification_data(df)

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    pipeline = build_classification_pipeline()

    pipeline.fit(x_train, y_train)

    y_pred = pipeline.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)
    feature_importance = get_feature_importances(pipeline)

    print("\nClassification Model Results:")
    print("-------------------------------")
    print(f"Accuracy: {accuracy:.4f}")

    print("\nClassification Report:")
    print(report)

    print("Confusion Matrix:")
    print(matrix)

    print("\nFeature Importance:")
    print(feature_importance)

    save_classification_report(
        accuracy,
        report,
        matrix,
        feature_importance
    )

    return pipeline


def get_feature_importances(pipeline):
    """
    Extracts feature importance values from the trained classification pipeline.
    """

    preprocessor = pipeline.named_steps["preprocessor"]
    model = pipeline.named_steps["model"]

    categorical_features = preprocessor.named_transformers_["cat"].get_feature_names_out(
        ["country", "gender"]
    )

    numerical_features = [
        "weight_kg",
        "body_length_cm",
        "latitude",
        "longitude"
    ]

    feature_names = list(categorical_features) + numerical_features

    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": model.feature_importances_
    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    return importance_df


def save_classification_report(accuracy, report, matrix, feature_importance):
    report_path = "data/output/ml/classification_report.txt"

    with open(report_path, "w") as file:
        file.write("Classification Model Results\n")
        file.write("-----------------------------\n")
        file.write(f"Accuracy: {accuracy:.4f}\n\n")

        file.write("Classification Report:\n")
        file.write(report)
        file.write("\n")

        file.write("Confusion Matrix:\n")
        file.write(str(matrix))
        file.write("\n\n")

        file.write("Feature Importance:\n")
        file.write(feature_importance.to_string(index=False))
        file.write("\n")

    print(f"\nClassification report saved to: {report_path}")
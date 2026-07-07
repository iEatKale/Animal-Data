import os
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from src.machine_learning.ml_preprocessing import build_preprocessor


def prep_regression_data(df):
    target_column = "body_length_cm"

    feature_columns = [
        "animal_type",
        "country",
        "weight_kg",
        "gender",
        "latitude",
        "longitude"
    ]

    x = df[feature_columns]
    y = df[target_column]

    return x, y


def build_regression_pipeline():
    categorical_features = [
        "animal_type",
        "country",
        "gender"
    ]

    numerical_features = [
        "weight_kg",
        "latitude",
        "longitude"
    ]

    preprocessor = build_preprocessor(
        categorical_features,
        numerical_features
    )

    model = RandomForestRegressor(
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


def train_regression_model(df):
    x, y = prep_regression_data(df)

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42
    )

    pipeline = build_regression_pipeline()

    pipeline.fit(x_train, y_train)

    y_pred = pipeline.predict(x_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)



    feature_importance = get_regression_feature_importances(pipeline)

    print("\nRegression Model Results:")
    print("--------------------------")
    print(f"Mean Absolute Error: {mae:.4f}")
    print(f"Root Mean Squared Error: {rmse:.4f}")
    print(f"R2 Score: {r2:.4f}")

    print("\nFeature Importance:")
    print(feature_importance)

    save_regression_report(
        mae,
        rmse,
        r2,
        feature_importance
    )

    return pipeline


def get_regression_feature_importances(pipeline):
    preprocessor = pipeline.named_steps["preprocessor"]
    model = pipeline.named_steps["model"]

    categorical_features = preprocessor.named_transformers_["cat"].get_feature_names_out(
        ["animal_type", "country", "gender"]
    )

    numerical_features = [
        "weight_kg",
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


def save_regression_report(mae, rmse, r2, feature_importance):
    report_path = "data/output/ml/regression_report.txt"

    with open(report_path, "w") as file:
        file.write("Regression Model Results\n")
        file.write("------------------------\n")
        file.write(f"Target: body_length_cm\n\n")

        file.write(f"Mean Absolute Error: {mae:.4f}\n")
        file.write(f"Root Mean Squared Error: {rmse:.4f}\n")
        file.write(f"R2 Score: {r2:.4f}\n\n")

        file.write("Feature Importance:\n")
        file.write(feature_importance.to_string(index=False))
        file.write("\n")

    print(f"\nRegression report saved to: {report_path}")
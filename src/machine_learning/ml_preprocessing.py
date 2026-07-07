from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


def build_preprocessor(categorical_features, numerical_features):
    """
    Reusable preprocessing step for ML pipelines.

    Categorical features are one-hot encoded.
    Numerical features are passed through unchanged.
    """

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
            ("num", "passthrough", numerical_features)
        ]
    )

    return preprocessor
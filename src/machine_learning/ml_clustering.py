import os
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


def prep_clustering_data(df):
    feature_columns = [
        "weight_kg",
        "body_length_cm",
    ]

    x = df[feature_columns]

    return x


def build_clustering_pipeline():
    # Builds a clustering pipeline using StandardScaler and KMeans.

    pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("model", KMeans(n_clusters=4, random_state=42, n_init=10))
        ]
    )

    return pipeline


def run_clustering_model(df):
    # Runs KMeans clustering and evaluates the resulting clusters.

    x = prep_clustering_data(df)

    pipeline = build_clustering_pipeline()

    cluster_labels = pipeline.fit_predict(x)

    clustered_df = df.copy()
    clustered_df["cluster"] = cluster_labels

    silhouette = silhouette_score(x, cluster_labels)

    cluster_counts = clustered_df["cluster"].value_counts().sort_index()

    cluster_comparison = pd.crosstab(
        clustered_df["cluster"],
        clustered_df["animal_type"]
    )

    print("\nClustering Model Results:")
    print("--------------------------")
    print(f"Silhouette Score: {silhouette:.4f}")

    print("\nCluster Counts:")
    print(cluster_counts)

    print("\nCluster vs Animal Type:")
    print(cluster_comparison)

    save_clustering_report(
        silhouette,
        cluster_counts,
        cluster_comparison
    )

    return clustered_df

def save_clustering_report(silhouette, cluster_counts, cluster_comparison):
    report_path = "data/output/ml/clustering_report.txt"


    with open(report_path, "w") as file:
        file.write("Clustering Model Results\n")
        file.write("------------------------\n")
        file.write("Model: KMeans\n")
        file.write("Number of clusters: 4\n\n")

        file.write(f"Silhouette Score: {silhouette:.4f}\n\n")

        file.write("Cluster Counts:\n")
        file.write(cluster_counts.to_string())
        file.write("\n\n")

        file.write("Cluster vs Animal Type:\n")
        file.write(cluster_comparison.to_string())
        file.write("\n")

    print(f"\nClustering report saved to: {report_path}")
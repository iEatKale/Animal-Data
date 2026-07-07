### Clustering Task

The final machine learning task focused on clustering. Unlike classification and regression, clustering is an unsupervised learning task. This means the model was not given a target column to predict.

The goal was to group animals based on patterns in the data and then compare the resulting clusters against the known `animal_type` values.

### Model Used

KMeans clustering was used for this task.

The model was created using:

```python
KMeans(n_clusters=4, random_state=42, n_init=10)
```

The number of clusters was set to 4 because the cleaned dataset contains four known animal types:

```text
European Bison
Hedgehog
Lynx
Red Squirrel
```

However, the model was not given the `animal_type` column during training. The animal type was only used afterwards to interpret the clusters.

### Features Used

The first version of the clustering model used:

```text
weight_kg
body_length_cm
latitude
longitude
```

This produced a weak clustering result:

```text
Silhouette Score: 0.1272
```

The low silhouette score suggested that the clusters were not well separated. The cluster comparison showed that Hedgehogs, Lynx, and Red Squirrels were spread across multiple mixed clusters.

This suggested that latitude and longitude were adding noise to the clustering process.

The model was then rerun using only physical measurements:

```text
weight_kg
body_length_cm
```

This produced a much stronger result:

```text
Silhouette Score: 0.8848
```

### Clustering Results

The final KMeans model produced the following cluster counts:

```text
cluster
0    617
1     42
2     16
3     73
```

The clusters were then compared against the known animal types:

```text
animal_type  European Bison  Hedgehog  Lynx  Red Squirrel
cluster
0                         0       277     2           338
1                        42         0     0             0
2                        16         0     0             0
3                         5         1    67             0
```

### Interpretation

The clustering results showed that the model grouped animals mainly by physical size rather than by exact animal type.

Cluster 0 contained mostly small animals:

```text
Hedgehogs
Red Squirrels
```

Clusters 1 and 2 contained only European Bison. This suggests that Bison were clearly separated from the other animals, but were split into two groups because they had a wider range of body weights and lengths.

Cluster 3 contained mostly Lynx, with a small number of other animals.

The results show that KMeans was effective at finding size-based groups in the dataset. However, it did not perfectly recreate the original animal type labels. This is expected because clustering is unsupervised and does not use the target labels during training.

### Silhouette Score

The silhouette score measures how well-separated the clusters are.

A score close to 1.0 means the clusters are well separated. A score close to 0.0 means the clusters overlap.

The final clustering model achieved:

```text
Silhouette Score: 0.8848
```

This indicates strong separation between the clusters when using only `weight_kg` and `body_length_cm`.

### Output

The clustering results are saved to:

```text
data/output/ml/clustering_report.txt
```

This file contains the silhouette score, cluster counts, and cluster comparison against the known animal types.
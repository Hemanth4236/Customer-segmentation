import pandas as pd

from src.data_preprocessing import (
    load_data,
    preprocess_data
)

from src.rfm_analysis import calculate_rfm

from src.pca_analysis import apply_pca

from src.clustering import perform_clustering

from src.visualization import plot_clusters

df = load_data("data/customers.csv")

df = preprocess_data(df)

rfm = calculate_rfm(df)

pca_data = apply_pca(
    rfm[['Recency',
         'Frequency',
         'Monetary']]
)

clusters = perform_clustering(pca_data)

rfm['Cluster'] = clusters

rfm.to_csv(
    "outputs/customer_segments.csv",
    index=False
)

plot_clusters(
    pca_data,
    clusters
)

print("Customer Segmentation Completed")
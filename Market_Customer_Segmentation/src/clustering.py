from sklearn.cluster import KMeans

def perform_clustering(data):

    model = KMeans(
        n_clusters=4,
        random_state=42
    )

    clusters = model.fit_predict(data)

    return clusters
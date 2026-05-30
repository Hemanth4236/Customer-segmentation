from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def apply_pca(data):

    scaler = StandardScaler()

    scaled = scaler.fit_transform(data)

    pca = PCA(n_components=2)

    pca_result = pca.fit_transform(scaled)

    return pca_result
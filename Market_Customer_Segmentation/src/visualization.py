import matplotlib.pyplot as plt

def plot_clusters(data, clusters):

    plt.figure(figsize=(8,6))

    plt.scatter(
        data[:,0],
        data[:,1],
        c=clusters
    )

    plt.title("Customer Segmentation")

    plt.xlabel("PCA1")

    plt.ylabel("PCA2")

    plt.savefig("outputs/cluster_plot.png")

    plt.show()
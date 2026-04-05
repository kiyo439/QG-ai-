import numpy as np
import pandas as pd
def load_iris_data(file_path="iris.csv"):
    df = pd.read_csv(file_path)
    # 提取4个特征
    X = df.iloc[:, :-1].values
    # 真实标签（仅用于评估）
    y_true = df.iloc[:, -1].values
    # 数据标准化
    X_mean = np.mean(X, axis=0)
    X_std = np.std(X, axis=0, ddof=1)
    X_norm = (X - X_mean) / X_std
    return X_norm, y_true, df


# ---------------------- 2. 手动实现K-Means ----------------------
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


def kmeans(X, K=3, max_iters=100, tol=1e-4):
    m, n = X.shape
    # 1. 初始化质心（随机选择K个样本）
    np.random.seed(42)
    centroids_idx = np.random.choice(m, K, replace=False)
    centroids = X[centroids_idx].copy()

    for _ in range(max_iters):
        # 2. E步：分配样本到最近簇
        clusters = [[] for _ in range(K)]
        for idx, x in enumerate(X):
            distances = [euclidean_distance(x, centroid) for centroid in centroids]
            cluster_idx = np.argmin(distances)
            clusters[cluster_idx].append(idx)

        # 3. M步：更新质心
        new_centroids = np.zeros((K, n))
        for cluster_idx, cluster in enumerate(clusters):
            if len(cluster) == 0:
                # 空簇，重新随机初始化
                new_centroids[cluster_idx] = X[np.random.choice(m)]
            else:
                new_centroids[cluster_idx] = np.mean(X[cluster], axis=0)

        # 4. 检查收敛
        centroid_diff = np.sum([euclidean_distance(centroids[i], new_centroids[i]) for i in range(K)])
        centroids = new_centroids
        if centroid_diff < tol:
            break

    # 生成簇标签
    labels = np.zeros(m)
    for cluster_idx, cluster in enumerate(clusters):
        for idx in cluster:
            labels[idx] = cluster_idx
    return labels, centroids, clusters


# ---------------------- 3. 模型评估 ----------------------
def sse(X, labels, centroids):
    # 簇内平方和，越小越好
    sse = 0
    for i, x in enumerate(X):
        centroid = centroids[int(labels[i])]
        sse += euclidean_distance(x, centroid) ** 2
    return sse


def silhouette_score(X, labels):
    # 轮廓系数，范围[-1,1]，越接近1越好
    m = X.shape[0]
    silhouette = np.zeros(m)
    for i in range(m):
        # 计算同簇样本平均距离a(i)
        same_cluster = X[labels == labels[i]]
        a = np.mean([euclidean_distance(X[i], x) for x in same_cluster if not np.array_equal(x, X[i])])
        # 计算最近异簇样本平均距离b(i)
        other_clusters = [X[labels == c] for c in np.unique(labels) if c != labels[i]]
        b = np.min([np.mean([euclidean_distance(X[i], x) for x in cluster]) for cluster in other_clusters])
        # 轮廓系数
        silhouette[i] = (b - a) / max(a, b)
    return np.mean(silhouette)


def purity_score(y_true, y_pred):
    # 纯度，衡量聚类与真实标签的匹配度，越高越好
    contingency = pd.crosstab(y_pred, y_true)
    return np.sum(np.max(contingency, axis=1)) / len(y_true)


# ---------------------- 4. 运行K-Means ----------------------
if __name__ == "__main__":
    X, y_true, df = load_iris_data()
    labels, centroids, clusters = kmeans(X, K=3)

    # 模型评估
    print("\n=== K-Means（鸢尾花聚类）评估结果 ===")
    print(f"簇内平方和(SSE): {sse(X, labels, centroids):.4f}")
    print(f"轮廓系数: {silhouette_score(X, labels):.4f}")
    print(f"聚类纯度: {purity_score(y_true, labels):.4f}")
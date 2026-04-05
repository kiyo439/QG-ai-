import numpy as np
import pandas as pd


# ---------------------- 1. 数据预处理（二分类标签） ----------------------
def load_wine_data(file_path="winequality-red.csv"):
    df = pd.read_csv(file_path, sep=",")
    # 提取特征X和标签y
    X = df.iloc[:, :-1].values  # 前11列特征
    y = df.iloc[:, -1].values  # 最后一列quality
    # 数据标准化（Z-score，消除量纲影响）
    X_mean = np.mean(X, axis=0)
    X_std = np.std(X, axis=0, ddof=1)
    X_norm = (X - X_mean) / X_std
    # 加偏置项（全1列）
    m = X_norm.shape[0]
    X_b = np.hstack([np.ones((m, 1)), X_norm])

    X_b = np.array(X_b, dtype=np.float64)
    y = np.array(y, dtype=np.float64)

    return X_b, y, df
def preprocess_logistic(X, y):
    # 质量>6为好酒（y=1），否则为坏酒（y=0）
    y_logi = (y > 6).astype(int)
    return X, y_logi


# ---------------------- 2. Sigmoid函数 ----------------------
def sigmoid(z):
    # 防止溢出
    z = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z))


# ---------------------- 3. 手动实现逻辑回归（梯度下降） ----------------------
def logistic_regression(X, y, alpha=0.01, epochs=10000):
    m, n = X.shape
    theta = np.zeros(n)  # 初始化参数
    for _ in range(epochs):
        z = X @ theta
        h = sigmoid(z)
        # 计算梯度
        gradient = (1 / m) * (X.T @ (h - y))
        # 更新参数
        theta -= alpha * gradient
    return theta


# ---------------------- 4. 预测与评估 ----------------------
def predict_logistic(X, theta, threshold=0.5):
    h = sigmoid(X @ theta)
    return (h >= threshold).astype(int)


def accuracy(y_true, y_pred):
    return np.mean(y_true == y_pred)


def confusion_matrix(y_true, y_pred):
    tp = np.sum((y_true == 1) & (y_pred == 1))
    tn = np.sum((y_true == 0) & (y_pred == 0))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    return np.array([[tn, fp], [fn, tp]])


def precision(y_true, y_pred):
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    return tp / (tp + fp) if (tp + fp) > 0 else 0


def recall(y_true, y_pred):
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    return tp / (tp + fn) if (tp + fn) > 0 else 0


def f1_score(y_true, y_pred):
    p = precision(y_true, y_pred)
    r = recall(y_true, y_pred)
    return 2 * p * r / (p + r) if (p + r) > 0 else 0


# ---------------------- 5. 运行逻辑回归 ----------------------
if __name__ == "__main__":
    X, y, df = load_wine_data()
    X_logi, y_logi = preprocess_logistic(X, y)
    theta_logi = logistic_regression(X_logi, y_logi, alpha=0.1, epochs=50000)
    y_pred_logi = predict_logistic(X_logi, theta_logi)

    # 模型评估
    print("\n=== 逻辑回归（好坏酒分类）评估结果 ===")
    print(f"准确率: {accuracy(y_logi, y_pred_logi):.4f}")
    print("混淆矩阵:")
    print(confusion_matrix(y_logi, y_pred_logi))
    print(f"精确率: {precision(y_logi, y_pred_logi):.4f}")
    print(f"召回率: {recall(y_logi, y_pred_logi):.4f}")
    print(f"F1分数: {f1_score(y_logi, y_pred_logi):.4f}")
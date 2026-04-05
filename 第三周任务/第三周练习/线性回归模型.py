import numpy as np
import pandas as pd

# ---------------------- 1. 数据加载与预处理 ----------------------
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


# ---------------------- 2. 手动实现线性回归（正规方程） ----------------------
def linear_regression(X, y):
    # 计算X^T X
    X_T = X.T
    X_T_X = X_T @ X
    # 求逆（加小正则项避免不可逆）
    X_T_X_inv = np.linalg.inv(X_T_X + 1e-8 * np.eye(X_T_X.shape[0]))
    # 计算最优参数theta
    theta = X_T_X_inv @ X_T @ y
    return theta


# ---------------------- 3. 预测与评估 ----------------------
def predict_linear(X, theta):
    return X @ theta


def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def rmse(y_true, y_pred):
    return np.sqrt(mse(y_true, y_pred))


def r2_score(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - ss_res / ss_tot


# ---------------------- 4. 运行线性回归 ----------------------
if __name__ == "__main__":
    X, y, df = load_wine_data()
    theta = linear_regression(X, y)
    y_pred = predict_linear(X, theta)

    # 模型评估
    print("=== 线性回归（红酒质量预测）评估结果 ===")
    print(f"MSE: {mse(y, y_pred):.4f}")
    print(f"RMSE: {rmse(y, y_pred):.4f}")
    print(f"R²: {r2_score(y, y_pred):.4f}")
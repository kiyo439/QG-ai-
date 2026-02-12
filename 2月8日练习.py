# numpy
# 创建一个形状为 (3,4) 的二维数组，元素为 0-11 的连续整数
# 查看数组的 shape 、 dtype 、 ndim 属性
# 将数组变形为 (4,3)，并展平为一维数组


import numpy as np

print("初始的数组是：")
arr = np.arange(12).reshape(3,4)
print(arr)

print(f"arr的形状是：{arr.shape}")
print(f"arr的类型是：{arr.dtype}")
print(f"arr的维度是：{arr.ndim}")

print("")
print("变换形状后的数组是：")
arr.resize((4,3))
print(arr)

print("")
print("展平后的一维数组是：")
arr.flatten()
print(arr)
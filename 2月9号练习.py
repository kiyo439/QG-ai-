# 处理 CSV 数据，以加州房价为例，使用pandas处理


# import pandas as pd
#
# csv_name = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
# housing_data = pd.read_csv(csv_name,sep=',')
# housing_data.to_csv("housing_data.csv",index=False)

# 配合 Matplotlib 画图，用 NumPy 生成 x 轴数据，绘制正弦曲线


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi,1000)
y = np.sin(x)

fig = plt.figure()
plt.plot(x,y)
plt.legend(['y=sin(x)'])
plt.title('y=sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

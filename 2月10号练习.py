# 泰坦尼克号数据集可视化
#     分别设计对各指标的生还数（率）进行对比可视化
#     分析可视化结果

# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# train = pd.read_csv(r'C:\Users\ZhuanZ\Desktop\pythonProject6\train.csv')

# sur = train['Survived'].value_counts()
# n=sur
# Sur = pd.DataFrame({
#     '是否幸存':sur.index,
#     '人数':sur.values
# })
# Sur['是否幸存']=Sur['是否幸存'].map({1:'幸存',0:'未幸存'})
# Sur=Sur.set_index('是否幸存')
# print("总体幸存人数情况：")
# print(Sur)
# print("")
#
# sur1 = train.groupby(by='Sex')['Survived'].value_counts()
# Sur1 = sur1.reset_index()
# Sur1.columns = ['性别','是否幸存','人数']
# Sur1['是否幸存']=Sur1['是否幸存'].map({1:'幸存',0:'未幸存'})
# Sur1['性别']=Sur1['性别'].map({'female':'女性','male':'男性'})
# Sur1=Sur1.set_index('性别')
# print("不同性别乘客生存情况：")
# print(Sur1)
# print("")
#
# print("不同入口幸存人数：")
# sur2 = train.groupby(by='Embarked')['Survived'].value_counts()
# Sur2 = sur2.reset_index()
# Sur2.columns = ['入口','是否幸存','人数']
# Sur2 = Sur2.set_index('入口')
# print(Sur2)
# print("")
#
# print("不同年龄段总人数：")
# age=train['Age']
# age_total,_=np.histogram(age,range=[0,80],bins=16)
# sur3=train['Age'].value_counts()
# Sur3=sur3.reset_index()
# Sur3.columns=['年龄','人数']
# Sur3=Sur3.set_index('年龄')
# Sur3=Sur3.sort_index()
# print(Sur3)
# print("")
# print("不同年龄段幸存人数")
# age_survived=[]
# for i in range(16):
#     n=train.loc[(age>=i*5) & (age<(i+1)*5)]['Survived'].sum()
#     print(f"{i*5}——{(i+1)*5}岁：{n}人")
#     age_survived.append(n)

# print("不同票价的幸存人数情况")
# sur4=train.groupby('Fare')['Survived'].value_counts()
# Sur4=sur4.reset_index()
# Sur4.columns=['票价','是否幸存','人数']
# tot=Sur4.groupby(by='票价')['人数'].sum()
# tot=tot.reset_index()
# tot.columns=['票价','总人数']
# survived=Sur4.groupby(by='票价')['是否幸存'].sum()
# survived=survived.reset_index()
# survived.columns=['票价','存活人数']
# print("存活人数：")
# survived=pd.merge(
#     left=tot,
#     right=survived,
#     on='票价'
# )
# print(survived)
# print("死亡人数：")
# death=Sur4.loc[Sur4['是否幸存']==0,['票价','人数']]
# death.columns=['票价','死亡人数']
# death=pd.merge(
#     left=tot,
#     right=death,
#     on='票价'
# )
# print(death)
# 可视化图表分析

# print("下面的是各项可视化分析相关图表：")
#
# print("总体生还几率如饼状图所示")
# print("")
# plt.figure(figsize=(6,6))
# plt.pie(
#     n,
#     autopct='%.2f%%',
#     labels=['未幸存','幸存'],
#     labeldistance=0.6,
#     pctdistance=0.4
# )
# plt.title('总体生存几率')
# plt.show(block=False)
# plt.pause(0.5)
#
# print("不同性别乘客的生存状况：")
# print("")
# plt.figure(figsize=(2*5,5))
# plt.title("不同性别乘客的生存状况")
# plt.axis('off')
# axes1=plt.subplot(1,2,1)
# axes1.pie(
#     Sur1.loc['女性']['人数'],
#     autopct='%.2f%%',
#     labels=['幸存','未幸存'],
#     labeldistance=0.6,
#     pctdistance=0.4
# )
# axes1.set_title('女性生还率')
# axes2=plt.subplot(1,2,2)
# axes2.pie(
#     Sur1.loc['男性']['人数'],
#     autopct='%.2f%%',
#     labels=['幸存','未幸存'],
#     labeldistance=0.6,
#     pctdistance=0.4
# )
# axes2.set_title('男性生还率')
# plt.show(block=False)
# plt.pause(0.5)
#
# plt.figure(figsize=(3*5,5))
# plt.title('不同出口乘客生存率')
# plt.axis('off')
# axes3=plt.subplot(1,3,1)
# axes3.pie(
#     Sur2.loc['C']['人数'],
#     autopct='%.2f%%',
#     labels=['幸存','未幸存'],
#     labeldistance=0.6,
#     pctdistance=0.4
# )
# axes3.set_title('C入口生还率')
# axes4=plt.subplot(1,3,2)
# axes4.pie(
#     Sur2.loc['Q']['人数'],
#     autopct='%.2f%%',
#     labels=['幸存','未幸存'],
#     labeldistance=0.6,
#     pctdistance=0.4
# )
# axes4.set_title('Q入口生还率')
# axes5=plt.subplot(1,3,3)
# axes5.pie(
#     Sur2.loc['S']['人数'],
#     autopct='%.2f%%',
#     labels=['幸存','未幸存'],
#     labeldistance=0.6,
#     pctdistance=0.4
# )
# axes5.set_title('S入口生还率')
# plt.show(block=False)

# print("不同年龄段幸存人数情况：")
# plt.figure(figsize=(12,6))
# plt.bar(
#     x=np.arange(2,78,5)+0.5,
#     height=age_total,
#     label='总人数',
#     alpha=0.8,
#     color='yellow',
#     width=5
# )
# plt.bar(
#     x=np.arange(2,78,5)+0.5,
#     height=age_survived,
#     label='幸存人数',
#     alpha=0.6,
#     color='blue',
#     width=5
# )
# plt.xticks(range(0,81,5))
# plt.yticks(range(0,121,10))
# plt.xlabel('年龄',position=(0.95,0))
# plt.ylabel('人数',position=(0,0.95))
# plt.title(' 不同年龄段总人数和幸存人数')
# plt.grid(alpha=0.4)
# plt.show(block=False)

# print("票价与生存率之间的关系：")
# death_rate=death['死亡人数'].div(death['总人数'])
# death_rate.index=death['票价']
# survived_rate=survived['存活人数'].div(survived['总人数'])
# survived_rate.index=survived['票价']
# plt.figure(figsize=(2*6,6))
# axes6=plt.subplot(1,2,1)
# axes6.scatter(
#     death_rate.index,
#     death_rate,
#     marker='o',
#     color='r'
# )
# plt.xlabel('票价')
# plt.ylabel('死亡率')
# axes6.set_title('死亡率与票价的关系')
# axes7=plt.subplot(1,2,2)
# axes7.scatter(
#     survived_rate.index,
#     survived_rate,
#     marker='^',
#     color='b'
# )
# plt.xlabel('票价')
# plt.ylabel('存活率')
# axes7.set_title('存活率与票价的关系')
# plt.show(block=True)
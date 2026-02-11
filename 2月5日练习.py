# 尝试用一行代码（推导式）生成 1 到 10 的平方数列表

# L =[ i*i for i in range(1,11)]
# print(L)

# 尝试用 map 结合 lambda 给全班同学的名字加上统一前缀（例如将 ["张三", "李四"]，变为 ["QG_张三", "QG_李四"] ）

# old_list =  ["张三", "李四"]
# new_list = map(lambda x : "QG_" + x,old_list)
# print(list(new_list))

# 能源核心数据清洗
# 数据： raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99",
# "120"] 。（可以自己设计数据）
# 实现自动跳过非数字项、仅保留≥80 数值、归一化为 0.xx-1.xx 小数，且根据结果是否 > 1.0
# 对应报「核心过载」或输出「运转正常」

# 方法一：

# raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99","120"]
# data1 = filter(lambda x: x.isnumeric(), raw_data)
# data2 = list(data1)
# new_data2 = [int(i) for i in data2]
# data3 = [i for i in new_data2 if i>=80]
# for i in range(len(data3)):
#     data3[i] = data3[i] / 100
#     if data3[i] > 1:
#         print(f"{data3[i]}:核心过载")
#     else:
#         print(f"{data3[i]}:运转正常")
# print(f"The new list is：{data3}")

# 方法二：

class InvaildValueError(Exception):
    def __init__(self, num):
        self.num = num
        super().__init__(f"{num}小于80，需要被筛选！")

raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99","120"]
new_data = []
for num in raw_data:
    try:
        num = int(num)
        if num < 80:
            raise InvaildValueError(num)
        new_data.append(num/100)
    except ValueError :
        print(f"{num}不是数字，需要被筛选！")
    except InvaildValueError as e:
        print(e)
print(new_data)
for num in new_data:
    if num > 1:
        print(f"{num}:核心过载")
    else:
        print(f"{num}:运转正常")
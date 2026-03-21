# import json
#
# def select_group_by_name(json_file_path, target_group_name):
#     with open(json_file_path, 'r', encoding='utf-8') as f:
#         json_data = json.load(f)
#
#     group_list = [json_data] if isinstance(json_data, dict) else json_data
#
#     for group in group_list:
#         # 检查当前group是否有group_name字段，且与目标一致
#         if "group_name" in group and group["group_name"] == target_group_name:
#             return group  # 匹配成功，返回该组完整内容
#
#     # 4. 未找到目标group
#     print(f"错误：未找到group_name为【{target_group_name}】的组！")
#     return None
#
#
# # ---------------------- 用法示例 ----------------------
# if __name__ == "__main__":
#     # 替换为你的JSON文件路径
#     JSON_PATH = "data(1).json"
#     # 替换为你要精准选择的group名称
#     TARGET_GROUP = "2d_task_2"
#
#     # 1. 精准选择目标group
#     target_group_data = select_group_by_name(JSON_PATH, TARGET_GROUP)
#
#     # 2. 提取该组的具体内容（哪怕字段名和其他组重复，也只取这一组的）
#     if target_group_data:
#         print(f"\n===== 选定【{TARGET_GROUP}】的内容 =====")
#         print(f"该组的vectors：{target_group_data['vectors']}")
#         print(f"该组的tasks：{target_group_data['tasks']}")
#         print(f"该组的ori_axis：{target_group_data['ori_axis']}")
import json
import numpy as np
import math

class Process:
    def __init__(self,axis,vectors = None):
        self.axis = [np.array(a).reshape(-1,1) for a in axis]
        self.vectors = [np.array(a).reshape(-1,1) for a in vectors]

    def axis_projection(self,vec = None):
        vecs = [np.array(vec).reshape(-1, 1)] if vec else self.vectors
        res = {}
        for v in vecs:
            proj = {
                "x轴投影": round(np.dot(v.T, self.axis[0])[0, 0] / np.linalg.norm(self.axis[0]), 4),
                "y轴投影": round(np.dot(v.T, self.axis[1])[0, 0] / np.linalg.norm(self.axis[1]), 4)
            }
            res[tuple(v.flatten())] = proj
        return res

    def axis_angle(self, vec=None):
        vecs = [np.array(vec).reshape(-1, 1)] if vec else self.vectors
        res = {}
        for v in vecs:
            norm_v = np.linalg.norm(v)
            if norm_v == 0:
                res[tuple(v.flatten())] = {"x轴夹角": 0.0, "y轴夹角": 0.0}
                continue
            # 先算投影，再求夹角
            proj = self.axis_projection(list(v.flatten()))[tuple(v.flatten())]
            angle = {
                "x轴夹角": round(math.acos(np.clip(proj["x轴投影"] / norm_v, -1, 1)), 4),
                "y轴夹角": round(math.acos(np.clip(proj["y轴投影"] / norm_v, -1, 1)), 4)
            }
            res[tuple(v.flatten())] = angle
        return res

    def area(self):
        return round(abs(np.linalg.det(np.hstack(self.axis))), 4)

    def change_axis(self, target_axis):
        # target_axis对应JSON中tasks的obj_axis: [[2,1],[1,2]]
        t_axis = [np.array(a).reshape(-1, 1) for a in target_axis]
        curr_mat = np.hstack(self.axis)
        t_mat = np.hstack(t_axis)
        return {
            tuple(v.flatten()): list((np.linalg.inv(t_mat) @ (curr_mat @ v)).flatten().round(4))
            for v in self.vectors
        }

def select_group(json_path,target_name):
    with open(json_path,"r",encoding="utf-8") as f:
        data = json.load(f)

    group_list = [data] if isinstance(data,dict) else data
    for group in group_list:
        if group["group_name"] == target_name:
            return group

    print(f"未找到名称为{target_name}的分组")
    return None

if __name__ == '__main__':
    json_path = "data(1).json"
    target_group_name = "2d_task_1"
    target_group = select_group(json_path,target_group_name)

    if target_group:
        cs = Process(
            axis = target_group['ori_axis'],
            vectors = target_group['vectors']
        )
        print(f"===== 【{target_group_name}】运算结果（匹配JSON中的tasks） =====")
        # 遍历JSON中的tasks，逐个执行对应运算
        for idx, task in enumerate(target_group["tasks"], 1):
            task_type = task["type"]
            print(f"\n{idx}. 任务类型：{task_type}")
            if task_type == "axis_angle":
                print("运算结果：", cs.axis_angle())
            elif task_type == "change_axis":
                # 提取JSON中该任务的obj_axis，作为目标坐标系
                target_axis = task["obj_axis"]
                print(f"   目标坐标系（obj_axis）：{target_axis}")
                print("   运算结果（变换后向量）：", cs.change_axis(target_axis))
            elif task_type == "area":
                print("   运算结果（面积缩放倍数）：", cs.area())
            elif task_type == "axis_projection":
                print("   运算结果：", cs.axis_projection())

import random
def list_random_maker (empty_list): # 隨機生成串列 每一個位置都隨機生成數字，放到空串列裡面 使用for迴圈
    ran_num = random.randint(3, 5)
    # print(ran_num)
    for i in range(ran_num):
        empty_list.append(random.randint(0, 101))
    return empty_list

list_random_result = list_random_maker([])
print(list_random_result)

personality_infor  = {'name': 'Willy', 'age': 27, 'birth year':1998}

def sort_list(lis):
    temp = 0
    for i in range(len(lis) - 1):
        if lis[i] > lis[i + 1]:
            temp = lis[i]
            lis[i] = lis[i + 1]
            lis[i + 1] = temp
    return lis

print(sort_list(list_random_result))



# def func1(name):
#     all_members = {
#         "悟空": [0, 0], "丁滿": [-1, 4], "特南克斯": [1, -2],
#         "弗利沙": [4, -1], "辛巴": [-3, 3], "貝吉塔": [-4, -1]
#     }
#     left = {"悟空", "特南克斯", "辛巴", "貝吉塔"}
#     right = {"丁滿", "弗利沙"}

#     if name not in all_members:
#         return None

#     # 取出目標
#     target_pos = all_members[name]
#     other_members = {k: v for k, v in all_members.items() if k != name} # 待分析
#     other_member = {}
#     for k, v in other_member.items():
#       if k != name:
#           other_member[k] = v

#     # 計算基礎距離
#     result = {
#         other: abs(pos[0] - target_pos[0]) + abs(pos[1] - target_pos[1])
#         for other, pos in other_members.items()
#     }

#     # 根據資料決定要 +2 的對象
#     if name in left:
#         # 目標在左邊 -> 右邊的人 +2
#         for other in right:
#             if other in result:
#                 result[other] += 2
#     elif name in right:
#         # 目標在右邊 -> 左邊的人 +2
#         for other in left:
#             if other in result:
#                 result[other] += 2

#     return result

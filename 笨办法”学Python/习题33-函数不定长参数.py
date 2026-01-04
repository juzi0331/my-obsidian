# 定义函数
# 需求:根据传入的数据,计算数据的最小值,最大值,平均值

# 位置参数 ---> *args --> 元组
# def calc_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     return min_data, max_data,round(avg_data ,1)
# # 调用函数
# data = calc_data(10,20,30,40,50)
# print(data)
# data = calc_data(111,222,333,444,555)
# print(data)

# 关键字参数 ---> *kwargs --> 字典
def calc_data(*args, **kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_datra = round(avg_data, kwargs.get("round"))

    if kwargs.get("print"):
        print("最小值:", min_data,"最大值:",max_data,"平均值:",avg_data)

    return min_data, max_data, avg_data

# 调用函数
print(calc_data(10, 20, 30, 40, 50, round=3,print=True))

print(calc_data(111, 222, 333, 444, 555, round=3,print=True))

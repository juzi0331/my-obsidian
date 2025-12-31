
# 🐍 Python 数据容器：字典 (Dictionary)

> [!ABSTRACT] Python 数据容器：字典 (Dictionary)
> 字典是一种存储**键值对 (Key-Value)** 类型数据的数据容器。
### 1. 字典介绍

- **核心逻辑**：通过唯一的 **键 (Key)** 找到对应的 **值 (Value)**。
- **生活类比**：字典中的“词条”对应 Key，“解释”对应 Value。

### 2. 定义语法与限制

- **基础语法**：`字典名称 = {key1: value1, key2: value2}`。
- **空字典**：`dict()` 或 `{}`。
- **强制规则**：
    1. **Key 唯一性**：键不能重复。如果出现重复，后面的值会**覆盖**前面的值。
    2. **Key 类型限制**：键必须是**不可变类型**（如 `str`, `int`, `float`, `tuple`），不能是列表、集合或字典。
    3. **Value 灵活性**：值可以是任何类型的数据。
### 3. 常用操作方法表

根据你的练习总结出以下核心方法：

|**操作分类**|**语法 / 方法**|**描述**|
|---|---|---|
|**新增/修改**|`dict[key] = value`|Key 不存在则新增，存在则修改|
|**删除 (通用)**|`del dict[key]`|直接从字典中移除该键值对|
|**删除 (带返回)**|`val = dict.pop(key)`|移除键值对并返回被删除的 **Value**|
|**常规获取**|`dict[key]`|获取值，若 Key 不存在会报错|
|**安全获取**|`dict.get(key)`|获取值，若 Key 不存在返回 `None` (不报错)|
### 4. 字典的查看与遍历

字典提供了三个核心视图方法用于不同场景的遍历：
- **`.keys()`**：获取字典中所有的键。
- **`.values()`**：获取字典中所有的值。
- **`.items()`**：获取所有的键值对（元组形式）。
```Python
# 遍历所有的键并取值
for k in dict1.keys():
    print(f"{k} : {dict1[k]}")
```
### 5. 综合实战：购物车管理系统

这是一个典型的**嵌套字典**应用：外层字典以“商品名”为 Key，内层字典存储价格和数量。
#### 核心逻辑拆解：
1. **添加逻辑**：使用 `if name in cart` 判断重复，防止误覆盖已有商品。
2. **修改逻辑**：先判断 `if name not in cart`，确保只修改已有的商品。
3. **数据解包**：在查询时，先通过键获取内层字典 `goods_info`，再访问其属性。

```Python
# 代码演示
shopping_Cart = {}  
menu = """  
######购物车系统######  
#    1.添加购物车    ##    2.修改购物车    ##    3.删除购物车    ##    4.查询购物车    ##    5.推出购物车    #####################  
"""  
while True:  
    # 1.1 制作菜单  
    print(menu)  
    # 1.2 执行操作  
    choice = input("请输入您的选择:")  
    match choice:  
        case "1":  # 添加购物车  
            goods_name = input("请输入商品名称:")  
            goods_price = float(input("请输入商品价格:"))  
            goods_num = int(input("请输入商品数量:"))  
            # 判断商品是否存在  
            if goods_name in shopping_Cart:  
                print("商品已存在")  
            else:  
                shopping_Cart[goods_name] = {"price": goods_price, "num": goods_num}  
                print("商品添加成功")  
        case "2":  # 修改购物车  
            goods_name = input("请输入要修改的商品名称:")  
            if goods_name not in shopping_Cart:  
                print("商品不存在,请重新选择")  
                continue  
            goods_price = float(input("请输入新的商品价格:"))  
            goods_num = int(input("请输入新的商品数量:"))  
        case "3":  # 删除购物车  
            goods_name = input("请输入要删除的商品名称:")  
            #  判断商品是否存在  
            if goods_name not in shopping_Cart:  
                print("商品不存在")  
            else:  
                del shopping_Cart[goods_name]  
                print("商品删除成功")  
        case "4":  # 查询购物车  
            goods_name = input("请输入要查询的商品:")  
  
            for goods_name in shopping_Cart.keys():  
                goods_info = shopping_Cart[goods_name]  
                print(f"商品的名称:{goods_name},商品的价格:{goods_info['price']}, 商品的数量{goods_info['num']}")  
        case "5":  # 退出购物车  
            break  
        case _:  
            print("输入错误")
```

### 💡 核心点总结

1. **字典 vs 列表**：列表适合有序存储，字典适合通过“标签”快速检索。
2. **安全性**：在执行 `del` 或访问 `[]` 之前，建议先用 `in` 关键字判断键是否存在。
3. **内存效率**：字典在 Python 3.7+ 中虽然保持了插入顺序，但其主要优势依然是 $O(1)$ 的超快速查找。

**优化说明：**

- **修正拼写**：修正了原笔记中 `dick1[k]` 的拼写错误为 `dict1[k]`。
- **逻辑补充**：在表格中明确区分了 `del` 和 `pop` 的差异。
- **结构分层**：将定义规则和操作方法分开，使笔记更符合“查阅手册”的风格。
--- 
![image.png](https://eo-picgo.xfc49.cn/python/20251224134611534.png)

---
![image.png](https://eo-picgo.xfc49.cn/python/20251224134733809.png)

---
![image.png](https://eo-picgo.xfc49.cn/python/20251224140946012.png)



# 🐍 Python 数据容器：集合 (Set) 详解

> [!ABSTRACT] Python 数据容器：集合 (Set) 
> 集合（Set）是 Python 中一种重要的数据容器，主要用于存储**不重复**的元素，常用于成员检测、去除重复项以及数学上的集合运算 1。

## 1. 集合的定义与基础特性

### 📝 基本定义

- **语法**：使用花括号 `{}` 或者 `set()` 函数 2。
- **特性**：
    - **无序性**：元素没有固定的顺序，因此**不支持下标索引访问** 3。
    - **唯一性**：集合内不允许出现重复的元素 4。
    - **可变性**：可以动态地向集合中添加或删除元素 5。

### ⚠️ 注意事项：如何定义空集合

- **正确方式**：必须使用 `set()` 6。
- **错误方式**：不能使用 `{}`，因为在 Python 中 `{}` 默认表示一个**空字典** 7。

```Python
# 定义有初始值的集合
s = {"1", "2", "3"} 

# 定义空集合
s2 = set() 
```

---

## 2. 核心数学运算

集合最强大的地方在于它能够高效地进行数学运算，如交集、并集和差集。

### 🔍 常用运算方法总结

|**运算类型**|**运算符**|**方法调用**|**描述**|
|---|---|---|---|
|**交集**|`&`|`s1.intersection(s2)`|找出同时存在于两个集合中的元素 8。|
|**并集**|`\|`|`s1.union(s2)`|合并两个集合，并自动去重 9。|
|**差集**|`-`|`s1.difference(s2)`|存在于 A 但不存在于 B 的元素 10。|

---

## 3. 实战案例：学生选课分析

通过你提供的代码逻辑，我们可以清晰地看到集合在处理复杂逻辑时的优势。

### 场景设定

已有四个集合，分别记录了选修 **足球、篮球、法语、艺术** 的学生名单 11。

### A. 找出同时选修了“法语”和“艺术”的学生（交集）

```Python
# 方式1：使用 intersection 方法
s1 = french_set.intersection(art_set) [cite: 1]

# 方式2：使用 & 运算符
s2 = french_set & art_set [cite: 1]
```

### B. 找出同时选修了“所有四门课程”的学生

```Python
# 连续使用 & 运算符进行多集合交集
s3 = football_set & basketball_set & french_set & art_set [cite: 1]
```

### C. 找出选修了“足球”但没有选修“篮球”的学生（差集）

```Python
# 方式1：使用 difference 方法
s4 = football_set.difference(basketball_set) [cite: 1]

# 方式2：使用 - 运算符
s5 = football_set - basketball_set [cite: 1]
```

---

## 4. 高级技巧与推导式

### 💡 集合推导式 (Set Comprehension)

当你需要根据某个规则快速生成集合时，推导式非常高效。

- **语法**：`{表达式 for 变量 in 可迭代对象 if 条件}` 12。

**代码实战：** 使用推导式实现差集逻辑 13：

```Python
s6 = {s for s in football_set if s not in basketball_set} [cite: 1]
```

### 📊 综合应用：统计每个学生的选课数量

这个逻辑使用了**并集**获取总名单，再利用**解包（Unpacking）**转化为列表进行计数。

1. 获取所有学生的去重总名单：
    `s7 = football_set | basketball_set | french_set | art_set` 14
2. 通过解包获取包含重复项的全量列表：
    `s8 = [*football_set, *basketball_set, *french_set, *art_set]` 15
3. **循环统计**：
```Python
  for i in s7:
    print(f"{i}选修了{s8.count(i)}门课程") [cite: 2]
```

---

## 5. 集合小结

- 如果你需要保证数据**不重复**且**不关心顺序**，首选集合 16。
- 集合的查询效率非常高（基于哈希表实现）。
- 在处理名单对比、共同好友推荐等场景时，使用 `&`、`|`、`-` 运算符会让代码异常简洁 17。


---

![image.png](https://eo-picgo.xfc49.cn/python/20251221124119265.png)

---

![image.png](https://eo-picgo.xfc49.cn/python/合集set常用方法.png)

---

![image.png](https://eo-picgo.xfc49.cn/python/set集合小结.png)
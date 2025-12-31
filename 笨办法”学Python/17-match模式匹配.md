
# 🐍 Python 流程控制：match 模式匹配

> [!ABSTRACT] Python 流程控制：match 模式匹配
`match` 语句是在 Python 3.10 中引入的结构化模式匹配功能，它类似于其他语言中的 `switch-case`，但功能远比其强大。

### 1. 基础语法结构

`match` 语句会接受一个表达式，并将其值与一个或多个 `case` 块中列出的模式进行比较。

```Python
match 变量:
    case 模式1:
        # 执行代码块
    case 模式2 | 模式3:
        # 多个模式匹配同一逻辑 (使用 | 运算符)
    case _ :
        # 通配符，匹配所有其他情况 (类似于 default)
```

---

### 2. 核心特性与实战示例

#### ⚡ 多模式匹配 (Or Pattern)

可以使用 `|` 符号将多个字面值组合在一起 2。

- **场景示例**：将周六和周日统一归类为“双休日” 3。

```Python
day = input("今天星期几:")
match day:
    case "1": print("星期一")
    case "2": print("星期二")
    case "3": print("星期三")
    case "4": print("星期四")
    case "5": print("星期五")
    case "6" | "7":  # 匹配 6 或 7
        print("双休日")
    case _:
        print("查询错误哦")
```

#### 🛡️ 模式守卫 (Guard Clause)

可以在 `case` 模式后添加 `if` 子句。只有当模式匹配**且** `if` 条件为真时，才会执行该分支 4。

- **场景示例**：在计算器中处理除法时，检查除数是否为 $0$ 5。

```Python
match oper:
    case "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
    # 或者更优雅的写法：
    case "/" if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
```

---

### 3. 综合案例：简易计算器

该案例展示了如何处理用户输入、数学运算以及异常边界情况 6。

```Python
num1 = float(input("请输入第一个数字:"))
num2 = float(input("请输入第二个数字:"))
oper = input("请输入运算符 (+, -, *, /):")

match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    case "/":
        print("错误：除数不能为 0")
    case _:
        print("不支持的运算符")
```

---

### 💡 笔记要点总结

1. **版本要求**：`match` 模式匹配仅支持 **Python 3.10** 及以上版本。
2. **执行顺序**：`match` 会从上到下依次匹配第一个符合条件的 `case` 块，执行完后直接退出 `match` 结构，不需要手动写 `break`。
3. **通配符 `_`**：必须放在最后一个 `case`，作为兜底逻辑 7。
4. **解包能力**：除了字面值匹配，`match` 还可以直接匹配列表、元组等复杂数据结构的解包（建议进阶学习）。
---

**优化说明：**
- **增加了数学公式**：对于除数不为 $0$ 等描述使用了 LaTeX 格式。
- **逻辑分层**：将多模式匹配和模式守卫分开讲解，便于查阅。
- **代码健壮性**：在计算器示例中补充了除数为 $0$ 的显式错误提示，使逻辑更完整。
---
![image.png](https://eo-picgo.xfc49.cn/python/20251213132757078.png)

---
![image.png](https://eo-picgo.xfc49.cn/python/20251213140359710.png)
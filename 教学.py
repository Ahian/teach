# 变量
a1 = 1
a2 = "a1的值:{}".format(a1)
# 布尔值真假，本质是1和0
a3 = True

# 数据结构
# 数组
array = [a1, a2, a3]
# dict字典
d1={
    "key1": a1,
    "key2": a2,
    "key3": a3,
}


def main():
    print(array[1])
    print(d1["key2"])


# 程序的入口
if __name__ == '__main__':
    main()

def argss(arg):
    # 变量
    a1 = 1
    a2 = "a1的值:{}".format(a1)
    # 布尔值真假，本质是1和0
    a3 = True

    # 数据结构
    # 数组 有顺序的一组变量
    array = [a1, a2, a3]
    # dict字典 和数组的核心区别是键值对
    d1 = {
        "key1": a1,
        "key2": a2,
        "key3": a3,
    }


def loop():
    # 循环
    var1 = 1
    while var1 < 888:
        var1 = var1 * 2
        print(var1)
    va2 = 1
    sum = 0
    while va2 <= 100:
        sum = sum + va2
        va2 = va2 + 1
        print(sum)


def loop_n(n):
    va2 = 1
    sum = 1
    while va2 <= n:
        sum = sum * va2
        va2 = va2 + 1
    return sum


def loop_n_2(n):
    va2 = 1
    sum = 0
    while va2 <= n:
        sum = sum + va2
        va2 = va2 + 2
    print(sum)


def logic():
    # 逻辑判断
    dic_compare = {
        "等于": "==",
        "不等于": "!=",
        "大于等于": ">=",
    }
    dic_logic = {
        "或": 'or',
        "并且": "and",
        "非": "not",
    }
    weather = 'sunny'

    if weather == 'sunny':
        print('running')
    else:
        print('no running')

        if 1:
            print('你是傻逼')
    price = 8
    if price < 5:
        print('买俩瓶')
    elif price > 5 and price >= 8:
        print('买一瓶')
    else:
        print('不买')


def ensure(arg1, arg2, massage):
    if arg1 != arg2:
        print(massage)
    else:
        print("没出错")


def big_ensure():
    ensure(loop_n(3), 6, "3出错")
    ensure(loop_n(4), 24, "4出错")
    ensure(loop_n(5), 100, "5出错")


def main():
    big_ensure()
    l4 = loop_n(4)
    print(l4)
    # 遍历一个数据结构


# 程序的入口
if __name__ == '__main__':
    main()

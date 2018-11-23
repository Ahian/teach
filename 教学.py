# 变量
a1 = 1
a2 = "a1的值:{}".format(a1)
# 布尔值真假，本质是1和0
a3 = True

# 数据结构
# 数组 有顺序的一组变量
array = [a1, a2, a3]
# dict字典 和数组的核心区别是键值对
d1={
    "key1": a1,
    "key2": a2,
    "key3": a3,
}


def main():
    # 逻辑判断
    dic_compare = {
        "等于": "==",
        "不等于":"!=",
        "大于等于":">=",
    }
    dic_logic = {
        "或": 'or',
        "并且": "and",
        "非":"not",
    }
    weather = 'sunny'

    if weather == 'sunny':
        print('running')
    else:
        print('no running')

    if 1:
        print('你是傻逼')



    price=8
    if price <5:
        print('买俩瓶')
    elif price>5 and price>=8 :
        print('买一瓶')
    else:
        print('不买')
# 程序的入口
if __name__ == '__main__':
    main()

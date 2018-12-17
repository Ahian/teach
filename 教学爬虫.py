# 网络请求库 用来给python上网
import requests
# 解析网页内容
from pyquery import PyQuery
# 导入操作系统库，用于文件读写
import os
# 导入xlwt xlrd 读写excel
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy

def write03Excel(dict):
    # excel文件路径
    path = '豆瓣电影.xls'
    r_xls = open_workbook(path) # 读取excel文件
    row = r_xls.sheets()[0].nrows # 获取已有的行数
    excel = copy(r_xls) # 将xlrd的对象转化为xlwt的对象
    # wb = xlwt.Workbook()
    # 第一次新建表头
    # sheet = wb.add_sheet("2003 job表")
    # value = [["name","salary","address","work_age","education","work_character","job_hashtag","job_welfare","job_description","job_skills","company","area","develophment","figure"],
    #          ]
    value = [i for i in dict.values()]
    table = excel.get_sheet(0)# 获取要操作的sheet
    for c in range(0,len(value)):
        table.write(row, c, value[c])
    # for i in range(0, 1):
    #     for j in range(0, len(value[i])):
    #         sheet.write(row, j, value[i][j])
    excel.save(path)
    print("写入数据成功！")


def process_page(page):
    # 把网页转换成dom对象
    dom = PyQuery(page)
    # 根据class查询
    items = dom('div.hd a')
    # 定义空数组用来装变量
    titles = []
    # 遍历items，逐个装进数组
    for i in items:
        s = PyQuery(i).text().split('  /')[0]
        titles.append(s)
    rating = dom('div.star')
    ratings = []
    # 遍历rating，逐个装进数组
    for i in rating:
        s = PyQuery(i).text().split(' ')[0]
        # 在ratings 追加s
        ratings.append(s)

    top = []
    length_of_list = len(titles)
    for i in range(length_of_list):
        d = {
            "name":titles[i],
            "rating":ratings[i]
        }
        write03Excel(d)
        top.append(d)
    return top

def existsed_cached(filename):
    folder = 'cached'
    # 用os API解决不同系统'/''\'的区别，cached\1.html
    path = os.path.join(folder, filename)
    # 没文件夹就建一个
    if not os.path.exists(folder):
        os.makedirs(folder)
    elif os.path.exists(path):
        with open(path, 'rb') as f:
            print('从',path, '读取数据中...')
            s = f.read()
            return s
    else:
        return None

def save(page,filename):
    folder = 'cached'
    path = os.path.join(folder, filename)
    with open(path, 'wb') as f:
        f.write(page)

def download(url):
    headers = {
        'user-agent': '''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8''',
    }
    r = requests.get(url, headers)
    print('网页的返回内容是这样：', r.content)
    page = r.content
    return page


def get_page(url):
    u1 = url.split('&')[0]
    filename = u1.split('=')[1] + '.html'
    print(filename)
    # 先根据链接切分文件名去本地找一下，有没有本地缓存
    page = existsed_cached(filename)
    # 如果没有本地缓存就要下载
    if page == None:
        page = download(url)
        # 下载完成后保存
        save(page,filename)
    return page



def main():
    print('已启动')
    url ='https://movie.douban.com/top250?start=25&filter='
    # 传一个链接,我就能得到页面
    page = get_page(url)
    # 把页面传进去处理，返回排行榜数组
    top = process_page(page)
    print(top)




if __name__ == '__main__':
    main()

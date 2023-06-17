import requests
import xlwt
import urllib.parse
from lxml import etree
import re
from fontTools.ttLib import TTFont

font = TTFont("file.ttf")
font.saveXML("font.xml")


# 字体处理
def get_dict():
    # 打开并读取font.xml
    with open('font.xml') as f:
        xml = f.read()

    # 正则表达式提取code和name
    keys = re.findall('<map code="(0x.*?)" name="uni.*?"/>', xml)
    values = re.findall('<map code="0x.*?" name="uni(.*?)"/>', xml)

    word_dict = {}
    # 将name解码成中文并作为值写入字典word_dict，该字典的键为keys
    for i in range(len(values)):
        if len(values[i]) < 4:
            values[i] = ('\\u00' + values[i]).encode('utf-8').decode('unicode_escape')
        else:
            values[i] = ('\\u' + values[i]).encode('utf-8').decode('unicode_escape')
        word_dict[keys[i]] = values[i]
    print(word_dict)
    return word_dict


dict = get_dict()

# 输入要爬取的岗位名称并转urlencode编码
job = input('请输入你要在实习僧爬取的实习岗位名称：')
job_urlencode = urllib.parse.quote(job)


# 注意：非专业反爬禁止更改本函数
def getPages():
    global all_page_num
    url = 'https://www.shixiseng.com/interns?keyword={}&city=%E5%85%A8%E5%9B%BD&type=intern'.format(job_urlencode)
    response = requests.get(url)
    response_text = response.text.replace('&#', '0')  # 将源码中&#xefed=>0xefed
    for key in dict:
        response_text = response_text.replace(key, dict[key])  # 0xefed格式=>对应的字典的值
    try:
        html_sxs_first_page = etree.HTML(response_text)
        all_page_num = html_sxs_first_page.xpath(
            '//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[8]/text()')[0]
        print("实习岗位{}共有{}页，预计需要等待：{}秒".format(job, all_page_num, all_page_num))
        print('------------------------------------------------------')
    except IndexError:
        print('------------------------------------------------------')
        print("网页索引过长，可能被反爬机制404")
        print('------------------------------------------------------')
    return int(all_page_num)


def spider_sxs():
    # 获取网页页数
    PageNum = getPages()
    # 创建execl并设置列名
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet1 = workbook.add_sheet('{}'.format(job))
    sheet1.write(0, 0, '职位名称')
    sheet1.write(0, 1, '工资')
    sheet1.write(0, 2, '城市')
    sheet1.write(0, 3, '出勤要求')
    sheet1.write(0, 4, '实习周期')
    sheet1.write(0, 5, '职位福利')
    sheet1.write(0, 6, '公司名称')
    sheet1.write(0, 7, '所属行业')
    sheet1.write(0, 8, '公司规模')
    sheet1.write(0, 9, '投递链接')

    # 设置excel列宽度
    sheet1.col(0).width = 256 * 30
    sheet1.col(1).width = 256 * 20
    sheet1.col(2).width = 256 * 10
    sheet1.col(3).width = 256 * 15
    sheet1.col(4).width = 256 * 15
    sheet1.col(5).width = 256 * 60
    sheet1.col(6).width = 256 * 20
    sheet1.col(7).width = 256 * 20
    sheet1.col(8).width = 256 * 15
    sheet1.col(9).width = 256 * 30

    sheet1_row = 0
    # 解析网页源代码
    for i in range(1, PageNum + 1):
        url = 'https://www.shixiseng.com/interns?page={}&type=intern&keyword={}&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend='.format(
            i, job_urlencode)
        print('第{}页的链接是：{}'.format(i, url))

        response = requests.get(url)
        response_text = response.text.replace('&#', '0')  # 将源码中&#xefed=>0xefed
        for key in dict:
            response_text = response_text.replace(key, dict[key])  # 0xefed格式=>对应的字典的值

        html_sxs = etree.HTML(response_text)
        all_div = html_sxs.xpath(
            '//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[1]//div[@class="intern-wrap intern-item"]')

        # 获取数据并存入excel
        for item in all_div:
            try:
                # 获取数据
                job_name = item.xpath('.//a[@class="title ellipsis font"]/text()')[0]  # 职位名称
                wages = item.xpath('.//span[@class="day font"]/text()')[0]  # 工资
                city = item.xpath('.//span[@class="city ellipsis"]/text()')[0]  # 城市
                week_time = item.xpath('.//span[@class="font"]/text()')[0]  # 出勤要求
                work_time = item.xpath('.//span[@class="font"]/text()')[1]  # 实习周期
                job_welfare = item.xpath('.//span[@class="company-label"]/text()')[0]  # 职位福利
                company_name = item.xpath('.//a[@class="title ellipsis"]/text()')[0]  # 公司名称
                company_type = item.xpath('.//span[@class="ellipsis"]/text()')[0]  # 所属行业
                company_size = item.xpath('.//span[@class="font"]/text()')[2]  # 公司规模
                job_href = item.xpath('.//a[@class="title ellipsis font"]/@href')[0]  # 投递链接

                # 向execl写入数据
                sheet1_row = sheet1_row + 1
                sheet1.write(sheet1_row, 0, job_name)
                sheet1.write(sheet1_row, 1, wages)
                sheet1.write(sheet1_row, 2, city)
                sheet1.write(sheet1_row, 3, week_time)
                sheet1.write(sheet1_row, 4, work_time)
                sheet1.write(sheet1_row, 5, job_welfare)
                sheet1.write(sheet1_row, 6, company_name)
                sheet1.write(sheet1_row, 7, company_type)
                sheet1.write(sheet1_row, 8, company_size)
                sheet1.write(sheet1_row, 9, job_href)
                # sheet1.write(sheet1_row, 10, company_href)

            except IndexError:
                'Error,please try once more!'

    workbook.save(r'.\data\实习僧{}岗位.xls'.format(job))
    print('爬取成功')
    print('------------------------------------------------------')


spider_sxs()

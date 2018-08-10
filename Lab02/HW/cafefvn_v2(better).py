from urllib.request import urlopen
from bs4 import BeautifulSoup
from operator import itemgetter
from youtube_dl import YoutubeDL
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)
content = conn.read().decode('utf-8')

soup  = BeautifulSoup(content, 'html.parser')

list_of_content = []

# Find bold line items
line_item_bold = soup.find_all('td', style = "width:32%;color:#014377;font-weight:bold;")
for li in line_item_bold:
    dic = {}
    
    li = li.string.strip().split(maxsplit = 1)
    li_key = float(li[0].strip('\''))
    dic['index'] = li_key

    li_value = li[1].strip('\'')
    dic['line item'] = li_value
    list_of_content.append(dic)

# Find values for bold line items
value_bold = soup.find_all('td', style = "width:15%;padding:4px;color:#014377;font-weight:bold;")

count = 0
for l in list_of_content:
    for i in range(4):
        l['Q' + str(i + 1)] = value_bold[count].string
        count += 1

list_temp = []

# Find normal line items
line_item = soup.find_all('td', style = "width:32%;color:#014377;")
for li in line_item:
    dic = {}
    
    li = li.string.strip().split(maxsplit = 1)
    li_key = float(li[0].strip('\''))
    dic['index'] = li_key

    li_value = li[1].strip('\'')
    dic['line item'] = li_value
    list_temp.append(dic)
    
#Find values for normal line items
value = soup.find_all('td', style = "width:15%;padding:4px;color:#014377;")

count = 0
for l in list_temp:
    for i in range(4):
        l['Q' + str(i + 1)] = value[count].string
        count += 1

# Merge 2 lists
list_of_content = list_of_content + list_temp

list_of_content = sorted(list_of_content, key = itemgetter('index'))

pyexcel.save_as(records = list_of_content, dest_file_name = 'bctc.xlsx')


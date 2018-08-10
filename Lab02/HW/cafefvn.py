from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)
content = conn.read().decode('utf-8')

soup  = BeautifulSoup(content, 'html.parser')

table_content = {}

# Find bold line items
line_item_bold = soup.find_all('td', style = "width:32%;color:#014377;font-weight:bold;")
for li in line_item_bold:
    li_list = []
    li = li.string.strip().split(maxsplit = 1)
    li_key = float(li[0].strip('\''))
    li_value = li[1].strip('\'')
    li_list.append(li_value)
    table_content[li_key] = li_list

# Find values for bold line items
value_bold = soup.find_all('td', style = "width:15%;padding:4px;color:#014377;font-weight:bold;")

count = 0
for v in table_content.values():
    for i in range(4):
        v.append(value_bold[count].string)
        count += 1

table_temp = {}

# Find normal line items
line_item = soup.find_all('td', style = "width:32%;color:#014377;")
for li in line_item:
    li_list = []
    li = li.string.strip().split(maxsplit = 1)
    li_key = float(li[0].strip('\''))
    li_value = li[1].strip('\'')
    li_list.append(li_value)
    table_temp[li_key] = li_list

#Find values for normal line items
value = soup.find_all('td', style = "width:15%;padding:4px;color:#014377;")

count = 0
for v in table_temp.values():
    for i in range(4):
        v.append(value[count].string)
        count += 1

# Merge 2 dictionaries
table_content.update(table_temp)

pyexcel.save_as(adict = table_content, dest_file_name = 'bctc.xlsx')


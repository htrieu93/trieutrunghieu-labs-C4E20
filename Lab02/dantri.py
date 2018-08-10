from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import pyexcel

# 1. Download web page
url = 'http://dantri.com.vn'
# 1.1 Create connection
# conn = urlopen(url)

# 1.2 Read
# data = conn.read()

# 1.3 Decode
# html_content = data.decode('utf-8')
# print(html_content)
html_content = urlopen('http://dantri.com.vn').read().decode('utf-8')
# print(html_content)

# write html to file
# f = open('dantri.html', 'wb')
# f.write(html_content)
# f.close()

# 2. Extract ROI (Region of Interest)
soup = BeautifulSoup(html_content, 'html.parser')

# find by class (default)
ul = soup.find(name = 'ul', attrs= {'ul1 ulnew'},)
# print(ul.prettify())

# 3. Extract data

li_list = ul.find_all('li')
li_dic = []

for li in li_list:
    # print(li.prettify())
    a = li.h4.a

    print(a.string)
    print(url + a['href'])
    print()
    dic = {
        'title' : a.string,
        'link' : url + a['href']
    }

    # Alternative way:
    # dic = {}
    # dic['title'] = a.string
    # dic['link'] = url + a['href']

    li_dic.append(dic)

pyexcel.save_as(records = li_dic, dest_file_name = 'dantri.xlsx')

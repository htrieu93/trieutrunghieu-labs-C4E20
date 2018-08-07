#20130075@student.hust.edu.vn
from gmail import *
import random as rand
from datetime import datetime

gmail = GMail('Hieu Trieu<hieutrieutrung93@gmail.com>', 'prototype101')

html_content = """ 
<p style="text-align: center;">Cộng h&ograve;a X&atilde; hội Chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc Lập Tự Do Hạnh Ph&uacute;c</p>
<p style="text-align: center;">&nbsp;</p>
<h3 style="text-align: center;"><strong>Đơn xin nghỉ học</strong></h3>
<p>Em chào thầy, em tên là Triệu Trung Hiếu</p>
<p>H&ocirc;m nay em viết mail này để xin thầy nghỉ học vì <em>{{sickness}}</em>.<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-sealed.gif" alt="sealed" /></p>
<p>&nbsp;</p>
<p style="text-align: right;">Em xin cảm ơn,</p>
<p style="text-align: right;"><span style="color: #ff0000;">Trung Hiếu</span></p>
<p>&nbsp;</p>
"""

excuses = ['bị ốm', 'mất xe đạp', 'về quê ăn giỗ', 'mưa ngập đường đi học']
sent_mail = True

current_time = str(datetime.time(datetime.now()))
current_hour = current_time[:5]

while current_hour > '07:00' and sent_mail:
    random_choice = rand.choice(excuses)

    html_content = html_content.replace('{{sickness}}', random_choice)

    msg = Message(
        'Test', 
        to = '20130075@student.hust.edu.vn',
        html = html_content
    )
    gmail.send(msg)

    sent_mail = False
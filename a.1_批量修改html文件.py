# -*- coding: utf-8 -*
#说明：①批量添加百度统计信息；②添加ico标志；③添加title和描述；④添加百度搜索

import os
import shutil
import json

class Html(object):
    def __init__(self, name='', title=''):
        self.name = name
        self.title = title

def obj_2_json(obj):
    return {
        "name": obj.name,
        "title": obj.title
    }

if __name__ == "__main__":
    basepath='涨粉邦/web/正式版本/html/'
    file_common=open('涨粉邦/补充/公共补充.txt', "r")
    shutil.copy('涨粉邦/补充/favicon.ico', basepath+'images/')
    content_add_common=file_common.read()  #获取需要添加的公告信息
    file_common.close()
    htmls = [Html('index','自媒体人聚集地'),Html('product','免费高效互粉工具')]
    json_html=json.dumps(htmls, default=obj_2_json,ensure_ascii=False)
    sucess_html=[]
    for html in htmls:
        filepath=basepath+html.name+'.html'
        file_add_title='<title>'+html.title+'</title><!--标题名称-->\n'  #添加每个页面标题信息
        file_html=open(filepath, "r",encoding="utf-8")
        content=file_html.read()
        pos = content.find('<title>')
        pos_delete =  content.find('<meta http-equiv="X-UA-Compatible" content="IE=edge"/>')
        if pos != -1:
            content_pre = content[:pos] + file_add_title +content_add_common+'\n'
            if pos_delete != -1:
                content_end=content[pos_delete:]
                content=content_pre+content_end
            file=open(filepath, "w",encoding="utf-8" )
            file.write(content)
            file.close()
            file_html.close()
            sucess_html.append(html.name)
    print(sucess_html)
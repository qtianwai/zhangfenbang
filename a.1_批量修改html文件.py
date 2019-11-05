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
    basepath='zfb/web/正式版本/html/'
    file_common=open('zfb/补充/公共补充.txt', "r")
    shutil.copy('zfb/补充/favicon.ico', basepath+'images/')
    content_add_common=file_common.read()  #获取需要添加的公告信息
    file_common.close()
    htmls = [Html('index','公众号涨粉资源及运营教程 - 涨粉邦'),Html('product','高效实用运营涨粉工具 - 涨粉邦'),Html('vip','加入会员免费获取全部资源 - 涨粉邦'),
             Html('course', '从零开始学运营教程分享 - 涨粉邦'),Html('material', '自媒体人运营必备网站和实用工具 - 涨粉邦')]
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
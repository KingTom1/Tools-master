# coding:utf-8
import urllib
import urllib.parse
import urllib.request
import base64
import json
import os

def get_access_token(ak,sk):
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(ak,sk)
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    j = json.loads(content)
    if (j['access_token']):
        return j['access_token']
    else:
        return ""
# 将数组中的字典分解 生成每行文字
def getstr(dicts):
    list1 = dicts['words_result']
    list2 = []
    result = ""
    for i in range(0,len(list1)):
        aa =list1[i]['words']
        list2.append(aa)
        result="\n".join(list2)
    return result

def gettxt(pngfile,tk):
    access_token = tk
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + access_token
    # 二进制方式打开图文件
    #r'E:\emrsharedoc\img\WST 500.1-2016.pdf\41.png'
    f = open(pngfile, 'rb')
    # 参数image：图像base64编码
    img = base64.b64encode(f.read())
    params = {"image": img}
    params = urllib.parse.urlencode(params).encode('utf-8')
    request = urllib.request.Request(url, params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content = response.read()
    return getstr(json.loads(content))

if __name__=="__main__":
    tk=get_access_token("tmoOldMGMKdGsZeVhel0Da7u", "vdks3D3aY3oGB4h31pDfBhKWqk1tX1aF")
    img_path='.\img'
    lst_imgfolders=['.\img']#os.listdir(img_path)
    for img_folder in os.listdir('.\img'):
        print(img_folder)
        print(img_folder.find('.JPG') >= 0)
        if img_folder.find('.JPG') >= 0 :
            img_file='.\img\\'+img_folder
            f=open(img_folder+'.txt','w',encoding='utf-8')
            f.writelines(gettxt(img_file,tk))
            f.close()



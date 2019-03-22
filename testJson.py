import json

def open_json():
    with open('Param.json',encoding='utf-8') as f:
        data=json.load(f)
        print(data,type(data))
        print(data['居住'],data['商业金融'])
        c=data['居住']
        print(c,type(c))
        print(c+3,c*5)
        print(data['规划年总人口']-data['规划年总就业'])

open_json()





# with open('Param.json', 'r') as json_file:
#     """
#     读取该json文件时，先按照gbk的方式对其解码再编码为utf-8的格式
#     """
#     data=json.loads(json_file)
#     print(data)
    # data = json_file.read().decode(encoding='gbk').encode(encoding='utf-8')
    #
    # result = json.loads(data)
    # new_result = json.dumps(result,ensure_ascii=False) # 参考网上的方法，***ensure_ascii***设为False
    # print (new_result)
# f=open('a.txt').encoding='gbk'
# # print(f)
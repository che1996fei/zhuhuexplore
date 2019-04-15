import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore' #构建url

#构建headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
html = requests.get(url, headers=headers).text #请求网页
doc = pq(html) #pyquery解析库的初始化
items = doc('.explore-tab .feed-item').items() #遍历
for item in items:
    question = item.find('h2').text() #获取h2的文本
    author = item.find('.author-link-line').text() #获取.author-link-line的文本
    answers = pq(item.find('.content').html()).text() #获取.content的文本
    file = open('explore.txt', 'a', encoding='utf-8') #以追加方式打开文件，并确定编码方式
    file.write('\n'.join([question, author, answers])) #写入
    file.write('\n' + '=' * 50 + '\n')
    file.close()

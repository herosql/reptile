import urllib.request
import uuid
from character_manipulation import character_manipulation
#下载类
class download:
    # 将图片储存到本地
    def image_download(imgList):
        for imag in imgList:
            image = imag.get_attribute("src")
            # 将远程数据下载到本地，第二个参数就是要保存到本地的文件名
            randomStr = 'E:/python/file/' + str(uuid.uuid4()) + image[character_manipulation.find_last(image, '.'):image.__len__()]
            urllib.request.urlretrieve(image, randomStr)
            print(randomStr, '正在下载。。。。。。。。。。')

    #将html储存到本地
    def html_download(title,content):
        randomStr = 'E:/python/file/' + title + '__' + str(uuid.uuid4()) + '.html'
        with open(randomStr, 'w') as f:
            f.write(content)
        print(randomStr, '正在下载。。。。。。。。。。')

#字符处理类
class character_manipulation:
    #获取字符串中特定字符最后出现的位置
    def find_last(string,str):
        last_position = -1
        while True:
            position = string.find(str,last_position+1)
            if position == -1:
                return last_position
            last_position = position

    #对链接进行校验
    def verify(herf,listurl):
        if herf is None:
            return False
        if 'http://www.xiuzhen123.com' in herf and herf not in listurl:
            return True
        else:
            return False

    #对链接进行处理
    def page_dispose(self,herf):
        x = herf[self.find_last(herf, '=') + 1:herf.__len__()]
        herfs = herf[0:self.find_last(herf, '=') + 1]
        x = self.get_sum_page(x) + 1
        herfs = herfs + str(x)
        return herfs

    #获取当前页码
    def get_page(self,herf):
        x = herf[self.find_last(herf, '=') + 1:herf.__len__()]
        return int(x)

    #获取总页码
    def get_sum_page(page):
        num = ''.join([x for x in page if x.isdigit()])
        return int(num)

    #获取当前帖子的id号
    def get_message_id(scr):
        sid = scr[character_manipulation.find_last(scr,'tid=') + 4:character_manipulation.find_last(scr,'&')]
        return sid

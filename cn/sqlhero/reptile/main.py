#开始爬取
from download import download
from character_manipulation import character_manipulation
from reptile import reptile
import time, threading

#连接主页
drint = reptile.get_connect('http://www.xiuzhen123.com')

main_list = []
def get_page_a(tr_list,main_list):
    for tr in tr_list:
        lista = tr.find_elements_by_tag_name('a')
        for a in lista:
            if character_manipulation.verify(a.get_attribute('href'),main_list):
                print(a.get_attribute('href'))
                main_list.append(a.get_attribute('href'))
# 修仙模块
funimax_lists = drint.find_elements_by_css_selector('#category_39 > table > tbody > tr')
get_page_a(funimax_lists,main_list)

# 道教模块
taoism_lists = drint.find_elements_by_css_selector('#category_49 > table > tbody > tr')
get_page_a(taoism_lists,main_list)

# 佛教模块
buddhism_lists = drint.find_elements_by_css_selector('#category_44 > table > tbody > tr')
get_page_a(buddhism_lists,main_list)

# 武功模块
kungfu_lists = drint.find_elements_by_css_selector('#category_36 > table > tbody > tr')
get_page_a(kungfu_lists,main_list)

# 修真门派模块
fix_true_factions = drint.find_elements_by_css_selector('#category_1 > table > tbody > tr')
get_page_a(fix_true_factions,main_list)

# 气功
qigong = drint.find_elements_by_css_selector('#category_51 > table > tbody > tr')
get_page_a(qigong,main_list)

# 内功
internal_work = drint.find_elements_by_css_selector('#category_46 > table > tbody > tr')
get_page_a(internal_work,main_list)

# 剑仙
sword_god = drint.find_elements_by_css_selector('#category_54 > table > tbody > tr')
get_page_a(sword_god,main_list)

# 法术
magic_arts = drint.find_elements_by_css_selector('#category_59 > table > tbody > tr')
get_page_a(magic_arts,main_list)

# 魔法
magic = drint.find_elements_by_css_selector('#category_93 > table > tbody > tr')
get_page_a(magic,main_list)

# 修真趣闻
coatard_interest = drint.find_elements_by_css_selector('#category_65 > table > tbody > tr')
get_page_a(coatard_interest,main_list)

#进入帖子
def into_forum_page(herf):
    herfs_connect = reptile.get_connect(herf)
    try :
        herfs_connect_title = herfs_connect.find_element_by_css_selector('#thread_subject')
        herfs_connect_ss = herfs_connect.find_element_by_css_selector('table[id^="pid"] > tbody > tr:nth-child(1) > td.plc > div.pct > div.pcb > div.t_fsz > table')
        download.html_download(herfs_connect_title.text, herfs_connect_ss.text)
    except Exception as e:
        print('网页结构发生改变')
    else:
        print('网页结构正常')
    finally:
        herfs_connect.close()

#进入论坛
def into_forum(herf,main_list):
    herf_connect = reptile.get_connect(herf)
    invitation_lists_a = herf_connect.find_elements_by_class_name('xst')
    for ass in invitation_lists_a:
        print(ass.get_attribute('href'))
        if character_manipulation.verify(ass.get_attribute('href'), main_list):
            into_forum_page(ass.get_attribute('href'))
    pagea = herf_connect.find_element_by_css_selector('#fd_page_top > div > label > span')
    pagea = character_manipulation.get_sum_page(pagea.text)
    #获取当前页码
    x = character_manipulation.get_page(character_manipulation,herf)

    # 关闭资源
    herf_connect.close()
    print('当前页码',x,'总页码',pagea)
    if x == pagea:
        return '完成第一个模块爬取！！！'
    else:
        herf = character_manipulation.page_dispose(character_manipulation,herf)
        into_forum(herf,main_list)

#关闭主页
drint.close()

#一遍筛选链接
for a in main_list:
    if 'http://www.xiuzhen123.com/forum.php?mod=forumdisplay&fid=' not in a:
        main_list.remove(a)

#二遍筛选链接
for a in main_list:
    if 'http://www.xiuzhen123.com/home.php?mod=space&username=' in a:
        main_list.remove(a)

#单线程爬取
for a in main_list:
    try:
        herfs = a + '&page=1'
        print('正在',into_forum(herfs, main_list))
    except Exception as e:
        continue
        print('网页结构发生改变')
    else:
        print('网页结构正常')



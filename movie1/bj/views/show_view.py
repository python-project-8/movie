import threading
# threading模块是Python里面常用的线程模块

from bj.spiders.s1 import *
from bj.spiders.s2 import *
from bj.spiders.s3 import *
from bj.spiders.s4 import *


def show_shce(res, supplier):

    print('=============================')
    print('数据提供商: {}'.format(supplier))

    for i in res:
        print(i)

def cateye_(*args):
    print('show',*args)
    ti = CatEye()
    res = ti.get_movie_from_time(*args)
    show_shce(res, '猫眼')

def nuomi_(*args):
    nm = Nuomi()
    res = nm.get_movie_from_nuomi(*args)
    show_shce(res, '糯米')

def taopp_(*args):
    tpp = TaoPiaoPiao()
    res = tpp.get_movie_from_taopp(*args)
    show_shce(res, '淘票票')

def meituan_(*args):
    mt = MeiTuan()
    res = mt.get_movie_from_meituan(*args)
    show_shce(res, '美团')


sup = [ nuomi_, taopp_, cateye_]

def _search(*a):

    Threads = []
    for i in sup:
        Threads.append(threading.Thread(target=i, args=(*a,)))

    for j in Threads:
        j.start()

    for k in Threads:
        k.join()

_search('上海', '闵行', '保利', '悟空')

# time_('上海', '闵行', '保利', '悟空')
# nuomi_('上海', '闵行', '保利', '悟空')
# taopp_('上海', '闵行', '保利', '悟空')
# meituan_('上海', '闵行', '保利', '悟空')

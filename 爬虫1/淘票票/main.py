from 淘票票.get_cities import TaoPP
from 淘票票.get_cinmal_length import *
from 淘票票.get_cinmal_href import *

def main():
    t = TaoPP()
    cities = t.city_list()
    page_len_list = run()
    tc = TaoPPCinemal()
    for i in range(len(cities)):
        city_code = cities[i]["城市编码"]
        city_name = cities[i]["城市名称"]
        tc.get_msg_save(int(page_len_list[i]), city_code)

if __name__ == '__main__':
    main()
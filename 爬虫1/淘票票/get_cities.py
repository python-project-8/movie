import requests
import fake_useragent

class TaoPP(object):
    UA = fake_useragent.UserAgent()

    def __init__(self):
        self.url = "https://www.taopiaopiao.com/cityAction.json?activityId&_ksTS=1553496785640_145&jsoncallback=jsonp146&action=cityAction&n_s=new&event_submit_doGetAllRegion=true"
        self.headers = {'User-Agent': self.UA.random}

    def get_response(self):
        r = requests.get(url=self.url, headers=self.headers)
        return r

    def city_list(self):
        city_codes_json = eval(self.get_response().text[11:-2])
        all_city_codes = city_codes_json['returnValue']
        city_msg_list = []

        for i in range(65, 91):
            if chr(i) in list(all_city_codes.keys()):
                start_city_codes = all_city_codes[chr(i)]
                for each_city in start_city_codes:
                    id = each_city['id']
                    region_name = each_city['regionName']
                    city_code = each_city['cityCode']

                    city_dict = {'城市id': id,
                                 '城市名称': region_name,
                                 '城市编码': city_code}
                    if city_dict not in city_msg_list:
                        city_msg_list.append(city_dict)

        return city_msg_list


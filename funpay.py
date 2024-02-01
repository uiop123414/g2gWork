from playwright.sync_api import sync_playwright
import requests
from bs4 import BeautifulSoup
import time
from LxmlSoup import LxmlSoup
from parsel import Selector

def funpay_fm(tmp_msg="",id_lot=25790923):
    cookies = {
            '_ym_uid': '170540091165735593',
            '_ym_d': '1705400911',
            'golden_key': '75dnbaap1acxn81rs7th0ge1qpi9q1jo',
            '_ym_isad': '2',
            '_gid': 'GA1.2.1784016697.1706638586',
            'PHPSESSID': 'jK4ZpTewWeGUU3-GgcuMMfsSo7%2CJ-nw7',
            'fav_games': '334-151-142-101-454-17',
            '_ga_STVL2Q8BNQ': 'GS1.1.1706640536.5.1.1706642534.0.0.0',
            '_ga': 'GA1.2.664365054.1705400912',
    }

    headers = {
            'authority': 'funpay.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': '_ym_uid=170540091165735593; _ym_d=1705400911; golden_key=75dnbaap1acxn81rs7th0ge1qpi9q1jo; _ym_isad=2; _gid=GA1.2.1784016697.1706638586; PHPSESSID=jK4ZpTewWeGUU3-GgcuMMfsSo7%2CJ-nw7; fav_games=334-151-142-101-454-17; _ga_STVL2Q8BNQ=GS1.1.1706640536.5.1.1706642534.0.0.0; _ga=GA1.2.664365054.1705400912',
            'origin': 'https://funpay.com',
            'referer': 'https://funpay.com/lots/offer?id='+str(id_lot),
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

    data = {
            'objects': '[{"type":"orders_counters","id":"9630111","tag":"55rwxq1y","data":false},{"type":"chat_counter","id":"9630111","tag":"lvu5uqp6","data":false},{"type":"chat_node","id":"users-6530674-9630111","tag":"k8990i3h","data":{"node":"users-6530674-9630111","last_message":0,"content":"Привет","offer_id":"lot:'+str(id_lot)+'","seller_id":6530674}}]',
            'request': '{"action":"chat_message","data":{"node":"users-6530674-9630111","last_message":0,"content":"'+tmp_msg+'","offer_id":"lot:'+str(id_lot)+'","seller_id":6530674}}',
            'csrf_token': 'r01ps7obvrpw23y9',
    }

    response = requests.post('https://funpay.com/runner/', cookies=cookies, headers=headers, data=data)

def get_funpay_pos(url:str='https://funpay.com/lots/offer?id=25652267'):
    req = requests.get(url=url)
    selector = Selector(text=req.text)
    
    price = selector.xpath('//html/body/div/div[1]/section/div[2]/div/div/div/div[2]/div/div[2]/form/div[1]/select/option[@class="hidden" and contains(@data-content, "от 33 360.49 ₽")]').get()

    print(price)


    soup = BeautifulSoup(req.content,'lxml')
    description = soup.select_one('.param-item h5:contains("Краткое описание") + div').get_text(strip=True)
    # Extract other parameters from the 'row' section
    param_rows = soup.select('.row .col-xs-6')
    parameters = {}
    for row in param_rows:
        try:
            key = row.select_one('.param-item h5').get_text(strip=True)
            value = row.select_one('.param-item .text-bold').get_text(strip=True)
            parameters[key] = value
        except AttributeError:
            break

    # Print or use the extracted information
    print(f"Price: {price}")
    print(f"Description: {description}")
    print("Other parameters:")
    for key, value in parameters.items():
        print(f"{key}: {value}")


get_funpay_pos()
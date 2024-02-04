from playwright.sync_api import sync_playwright
import requests
from bs4 import BeautifulSoup
from parsel import Selector
from currency_converter import CurrencyConverter
from translator import translate
import asyncio


def get_funpay_pos(url:str='https://funpay.com/lots/offer?id=25652267'):
    req = requests.get(url=url)
    selector = Selector(text=req.text)
    try:
        price = float(selector.xpath('//html/body/div/div[1]/section/div[2]/div/div/div/div[2]/div/div[2]/form/div[1]/select/option[1]').get().split(" ₽")[0].split('class="payment-value"&gt;от')[-1].replace(' ',''))
    except AttributeError:
        print("Empty offer")
        
    price = round(CurrencyConverter().convert(price,'RUB','EUR'),2)
    print(price,'$')


    soup = BeautifulSoup(req.content,'lxml')
    description = translate(soup.select_one('.param-item h5:contains("Краткое описание") + div').get_text(strip=True))
    
    full_description = translate(soup.select_one('.param-item h5:contains("Подробное описание") + div').get_text(strip=True))

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

    return {'price':price,'desc':description,'full_desc':full_description,'other_params':param_rows}


async def funpay_check(url:str):
    """
    True - is not exists 
    False - exits
    """
    req = requests.get(url=url)
    selector = Selector(text=req.text)
    text = selector.xpath('//html/body/div/div[1]/section/div[2]/div/div[1]/div/div/p').get()

    if text != None and 'Предложение устарело, было удалено или не существовало вовсе.' in text:
        return True
    return False


if __name__ == "__main__":
    print(asyncio.run(funpay_check('https://funpay.com/lots/offer?id=25790923')))
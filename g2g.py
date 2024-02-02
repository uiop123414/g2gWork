import json
from playwright.async_api import async_playwright
import time
from bs4 import BeautifulSoup
import asyncio
def g2g_fm(page,name):

    page.locator(f'div:text("{name}")').click()
    time.sleep(5)
    page.locator('xpath=//html/body/div[1]/div/div/div/div[3]/div[2]/div/div/div/div[3]/div/div/div[2]/form/div[1]/div/div[2]/div/p').click()
    page.keyboard.type('Default message')
    page.locator('xpath=//html/body/div[1]/div/div/div/div[3]/div[2]/div/div/div/div[3]/div/div/div[2]/form/div[2]/div[2]/button/span[2]').click()    
    time.sleep(5)
        # Save the cookies
def extract_data_from_span(span):
    badge = span.find('div', {'class': 'q-badge'})
    if badge:
        return int(badge.text)
    else:
        return 0

async def get_messages():
    data_dir = "./data1/"
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(headless = False,user_data_dir=data_dir)
        try:

            # Load the cookies
            with open(data_dir+"cookies.json", "r") as f:
                cookies = json.loads(f.read())
                browser.add_cookies(cookies)
        except (FileNotFoundError,json.decoder.JSONDecodeError):
            print('No cookies')
        page = await browser.new_page()
        await page.goto("https://www.g2g.com/chat/#/")
        time.sleep(100)
        # Wait for the element to be present
        page.wait_for_selector('//html/body/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[2]/div/div[1]')
        # Get the inner HTML of the specified element
        inner_html = await page.inner_html('//html/body/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[2]/div/div[1]')
        soup = BeautifulSoup(inner_html, 'html.parser')
        spans = soup.find_all('span', {'id': lambda x: x and x.startswith('channel-item')})


        result_list = []

        for span in spans:
            username = span.find('div', {'class': 'text-body1'}).text.strip()
            unread_msg = extract_data_from_span(span)
            
            result_list.append({'username': username, 'unread_msg': unread_msg})

        ls = list()

        for item in result_list:
            if item['unread_msg'] > 0:
                ls.append({'username':item['username'],'messages':await g2g_unread_message(page,item['username'],item['unread_msg'])})
        
        return ls

async def g2g_create_offer(data:dict={}):
    
    data_dir = "./data1/"
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(headless = False,user_data_dir=data_dir)
        try:

            # Load the cookies
            with open(data_dir+"cookies.json", "r") as f:
                cookies = json.loads(f.read())
                browser.add_cookies(cookies)
        except (FileNotFoundError,json.decoder.JSONDecodeError):
            print('No cookies')
        page = await browser.new_page()
        await page.goto("https://www.g2g.com/sell/index",timeout=0)
    

        time.sleep(1000)



async def g2g_unread_message(page,name,unread_msg):
    await page.locator(f'div:text("{name}")').click()
    time.sleep(5)
    await page.locator('xpath=//html/body/div[1]/div/div/div/div[3]/div[2]/div/div/div/div[3]/div/div/div[2]/form/div[1]/div/div[2]/div/p').click()

    page.wait_for_selector('//html/body/div[1]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div')
    inner_html = await page.inner_html('//html/body/div[1]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div')

    soup = BeautifulSoup(inner_html, 'html.parser')

    # Find all chat messages
    chat_messages = soup.find_all('div', class_='g-chat-message')

    # Extract relevant information from each message
    message_list = []
    chat_messages.reverse()


    for message,_ in zip(chat_messages,range(unread_msg)):
        try:
            timestamp = message.find('div', class_='text-secondary').text.strip()
            message_content = message.find('div', class_='q-markdown').text.strip()
            
            # Check if the message is about an order
            is_order_message = 'Order' in message_content
            
            # Add information to the list
            message_list.append({
                'timestamp': timestamp,
                'content': message_content,
                'is_order_message': is_order_message,
            })
        except AttributeError:
            print('first msg')
            

    return message_list

if __name__ == '__main__':
    asyncio.run(g2g_create_offer())
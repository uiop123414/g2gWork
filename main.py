from g2g import get_messages
from funpay import funpay_fm,get_funpay_pos
from tg_part import start_bot ,echo_message,bot
import asyncio
import json

async def main():
    print('Start work')
    while True:
        print('Start work')
        ls = await get_messages()
        if ls != []:
            for item in ls:
                text_msg = "Nickname "+item['username']+'\nMessage: '
                for message in item['messages']:
                    text_msg +=message['content']+'\n'
                # text_msg += 'Url: '+item['url']
                await echo_message(bot,text_msg)

# asyncio.run(main())

get_funpay_pos('https://funpay.com/lots/offer?id=24666646')
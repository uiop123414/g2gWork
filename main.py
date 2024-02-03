from g2g import get_messages
from funpay import get_funpay_pos
from tg_part import start_bot ,echo_message,bot ,check
import asyncio

async def main():
    print('Start work')
    while True:
        print('Start work')
        ls = await get_messages()
        if ls != []:
            for item in ls:
                text_msg = "Nickname "+item['username']
                for message in item['messages']:
                    text_msg +='\nMessage: '+message['content']
                # text_msg += 'Url: '+item['url']
                await echo_message(bot,text_msg)
                await check(bot)

asyncio.run(main())

# get_funpay_pos('https://funpay.com/lots/offer?id=24666646')
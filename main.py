from g2g import get_messages, g2g_fm
from tg_part import echo_message, bot ,check
import asyncio

async def main():
    print('Start work')
    while True:
        print('Start work')
        ls = await get_messages()
        if ls != [] and ls != None:
            for item in ls:
                #SEND FIRST MESSAGE 
                await g2g_fm(item['username'])
                
                
                #CHECH FOR NEW MESSAGES
                text_msg = "Nickname "+item['username']
                for message in item['messages']:
                    text_msg +='\nMessage: '+message['content']
                # text_msg += 'Url: '+item['url']
                await echo_message(bot,text_msg)
        #CHECK FUNPAY ORDER EXISTS        
        await check(bot)

asyncio.run(main())

# get_funpay_pos('https://funpay.com/lots/offer?id=24666646')
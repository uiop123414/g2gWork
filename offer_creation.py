import playwright
import time



async def account_Dota2(page,data:dict):
    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/span/label/div/div/div/div/div/button').click()
    await page.get_by_text('FaceIT Ready').click()

    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/span/label/div/div/div/div/div/button').click()
    await page.get_by_text(data['mmr']).click()

    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[1]/div[1]/div/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/span/label/div/div/div/div/div/button').click()
    await page.get_by_text(data['behavior']).click()


    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[7]/div/div/div/div[2]/button/span[2]').click()


async def account_EFT(page,data:dict):
    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/span/label/div/div/div/div/div/button/span[2]/span').click()
    await page.get_by_text(data['level']).click()

    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/span/label/div/div/div/div/div/button/span[2]/span').click()
    await page.get_by_text(data['edition']).click()



async def account_CS(page,data:dict):
    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/span/label/div/div/div/div/div/button/span[2]/span').click()
    await page.get_by_text(data['prime']).click()

    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/span/label/div/div/div/div/div/button/span[2]/span/div/div[1]').click()
    await page.get_by_text(data['type']).click()

    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[1]/div[1]/div/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/span/label/div/div/div/div/div/button/span[2]/span/div/div[1]').click()
    await page.get_by_text(data['rating']).click()

    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[1]/div[1]/div/div/div[2]/div[2]/div[4]/div/div[2]/div[1]/div/span/label/div/div/div/div/div/button/span[2]').click()
    await page.get_by_text(data['rank']).click()

    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[1]/div[1]/div/div/div[2]/div[2]/div[5]/div/div[2]/div[1]/div/span/label/div/div/div/div/div/button/span[2]/span/div/div[1]').click()
    await page.get_by_text(data['medals']).click()

async def account_Val(page,data:dict):
    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/span/label/div/div/div/div/div/button/span[2]/span/div/div[1]').click()
    await page.get_by_text(data['server']).click()

    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/span/label/div/div/div/div/div/button/span[2]/span/div/div[1]').click()
    await page.get_by_text(data['type']).click()

    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[1]/div[1]/div/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/span/label/div/div/div/div/div/button/span[2]/span/div/div[1]').click()
    await page.get_by_text(data['rank']).click()

    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[1]/div[1]/div/div/div[2]/div[2]/div[4]/div/div[2]/div[1]/div/span/label/div/div/div/div/div/button/span[2]/span/div/div[1]').click()
    await page.get_by_text(data['agents']).click()

    await page.locator('xpath=/html/body/div[1]/div/div[1]/main/div[3]/form/div/div[1]/div[1]/div/div/div[2]/div[2]/div[5]/div/div[2]/div[1]/div/span/label/div/div/div/div/div/button/span[2]/span/div/div[1]').click()
    await page.get_by_text(data['skins']).click()
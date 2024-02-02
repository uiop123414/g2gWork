import requests
import json

def translate(text:str):
    #https://cloud.yandex.com/ru/docs/iam/operations/iam-token/create#api_1
    IAM_TOKEN = get_IAM_TOKEN()
    folder_id = 'b1gv13ghfh7selgeug5k'
    target_language = 'en'
    texts = [text]

    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }

    response = json.loads(requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
        json = body,
        headers = headers
    ).text)
    return response['translations'][0]['text']

def get_IAM_TOKEN():

    url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"
    headers = {"Content-Type": "application/json"}

    data = {
        "yandexPassportOauthToken": "y0_AgAAAAAWU2FxAATuwQAAAAD5sFk-AABjEc2ox4hJBrlaJBMUr4X6yCsLog"
    }

    response = requests.post(url, json=data, headers=headers)


    return response.json()['iamToken']

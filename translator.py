import requests
import json

def translate(text:str):
    IAM_TOKEN = "t1.9euelZrNyZrHm4vOy4uVi5vLz8uMke3rnpWalZ3KmZuex5STl8iNk8nImZbl8_ccFRBS-e9oZzZ9_N3z91xDDVL572hnNn38zef1656VmpOcj8aKyszNis2Zjc6MzM3O7_zF656VmpOcj8aKyszNis2Zjc6MzM3O.9LxP-JU-2gtGM-KFpWLUAWfpYHm0kw2n4CQPn16Wo6sd2hfpp0eB578Zf2MJwm6f42ORZwGE8mSOMreE8rIqCg"
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

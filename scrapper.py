from traceback import format_exc
import requests
from loguru import logger

class Scrapper:
    
    def __init__(self):
        self.session = requests.Session()
        self.response = None

    def send_get_request(self, url, params={}, headers={}, cookies={}):
        try:
            response = requests.post(
                url=url,
                params=params,
                headers=headers,
                cookies=cookies
            )
        except Exception as err:
            logger.error('리퀘스트 에러 발생')
            logger.error(err)
            logger.error(format_exc())
            return 0
        else:
            self.response = response
            return 1
        
    def send_post_request(self, url, data={}, headers={}, cookies={}):
        try:
            response = requests.post(
                url=url,
                data=data,
                headers=headers,
                cookies=cookies
            )
        except Exception as err:
            logger.error('리퀘스트 에러 발생')
            logger.error(err)
            logger.error(format_exc())
            return 0
        else:
            self.response = response
            return 1
        

# https://auth.data.go.kr/sso/login
'''
clientId
: 
"hagwng3yzgpdmbpr2rxn"
password
: 
""
redirectUrl
: 
"https://data.go.kr/sso/profile.do"
username
: 
""
_csrf
: 
"c9b46cd3-3200-4b87-82a2-1b7e4cfa6042"
'''
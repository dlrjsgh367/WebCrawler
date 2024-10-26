from scrapper import Scrapper

def test_send_get_request():
    sc = Scrapper()
    url = 'https://jd-inia.tistory.com/32'
    res = sc.send_get_request(
        url=url
    )
    print(res.text)
    assert res != 0

def test_send_post_request():
    sc = Scrapper()
    url = 'https://auth.data.go.kr/sso/login'
    res = sc.send_post_request(
        url=url
    )
    print(res.text)
    assert res != 0

if __name__ == '__main__':
    test_send_get_request()

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
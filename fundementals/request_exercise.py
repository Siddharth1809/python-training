import requests
from requests import Response


def requests_get_method():
    response = requests.get('https://xkcd.com/353/')
    print(response)
    print(response.text)


def requests_get_image():
    response = requests.get('https://imgs.xkcd.com/comics/python.png')
    print(response.content)
    print(response.status_code)
    print(response.ok)

    with open('comic.png', 'wb') as f:
        f.write(response.content)

    print(response.headers)


def requests_get_args():
    payload = {'page': 2, 'count': 25}

    response = requests.get('http://httpbin.org/get', params=payload)

    print(response.text)

    print(response.url)


def requests_post_json():
    payload = {'username': 'abc', 'password': 'test'}
    response = requests.post('http://httpbin.org/post', data=payload)

    print(response.text)

    # json data
    response_dict = response.json()
    print(response_dict)


def requests_authorization():
    response = requests.get('http://httpbin.org/basic-auth/abc/test', auth=('abc', 'test'))
    print(response)
    print(response.text)


def requests_authorization_false():
    response = requests.get('http://httpbin.org/basic-auth/abc/test', auth=('abcd', 'test'))
    print(response)
    print(response.text)  # don't print anything if auth is wrong


def response_timeout():
    response = requests.get('https://httpbin.org/delay/6', timeout=3)
    print(response)


# session objects
def session_object():
    session = requests.Session()
    session.cookies.update({'visit-month': 'July'})

    response_one = session.get('http://httpbin.org/cookies')
    print(response_one.text)
    # prints information about "visit-month" cookie

    response_two = session.get('http://httpbin.org/cookies', cookies={'visit-year': '2017'})
    print(response_two.text)
    # prints information about "visit-month" and "visit-year" cookie

    response_three = session.get('http://httpbin.org/cookies')
    print(response_three.text)
    # prints information about "visit-month" cookie


# sending cookies amd headers
def cookie_header():
    url = 'http://some-domain.com/set/cookies/headers'

    response = requests.get(url)
    print(response.headers)

    headers = {'user-agent': 'your-own-user-agent/0.0.1'}
    cookies = {'visit-month': 'February'}
    response_one = requests.get(url, headers=headers, cookies=cookies)

    print(response_one)

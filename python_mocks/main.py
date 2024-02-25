import requests

def add(a, b):
    return a + b

def len_joke():
    joke = get_joke()
    return len(joke)

def get_joke():
    url = 'http://api.icndb.com/jokes/random'
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()['value']['joke']
    else:
        joke = 'No jokes'
    return joke

def get_pro_joke():
    url = 'http://api.icndb.com/jokes/random'

    # print(type(requests.exceptions.Timeout))

    try:
        response = requests.get(url)
    except requests.exceptions.Timeout:
        return 'No jokes'
    except requests.exceptions.ConnectionError:
        pass
    if response.status_code == 200:
        joke = response.json()['value']['joke']
    else:
        joke = 'No jokes'
    return joke

if __name__ == '__main__':
    print(get_joke())
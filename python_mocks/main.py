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

def pro_get_joke():
    url = 'http://api.icndb.com/jokes/random'

    # print(type(requests.exceptions.Timeout))

    try:
        response = requests.get(url, timeout=30)
    except requests.exceptions.Timeout:
        return 'Timeout Error'
    except requests.exceptions.ConnectionError:
        pass
    if response.status_code == 200:
        joke = response.json()['value']['joke']
    else:
        joke = 'No jokes'
    return joke

def advance_get_joke():
    url = 'http://api.icndb.com/jokes/random'

    # print(type(requests.exceptions.Timeout))

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

    except requests.exceptions.Timeout:
        return 'Timeout Error'
    
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.HTTPError: 
        return 'HTTPError was raised'
    else:
        if response.status_code == 200:
            joke = response.json()['value']['joke']
        else:
            joke = 'No jokes'
    return joke

def next_level_get_joke():
    url = 'http://api.icndb.com/jokes/random'

    # print(type(requests.exceptions.Timeout))

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

    except requests.exceptions.Timeout:
        return 'Timeout Error'
    
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code

        if status_code in [503, 504]:
            pass
        else:
            pass   
        return 'HTTPError was raised'
    else:
        if response.status_code == 200:
            joke = response.json()['value']['joke']
        else:
            joke = 'No jokes'
    return joke

if __name__ == '__main__':
    print(get_joke())
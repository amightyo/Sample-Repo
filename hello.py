import requests


if __name__ == "__main__":
    r = requests.get('http://gralswerk.org')
    print(r.status_code)
    print(r.ok)

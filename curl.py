from time import sleep
import requests

def curl(domain):

    curl_server = 'https://helloacm.com/api/curl/?url='

    # https://helloacm.com/api/curl/?url=
    base_url = server + str(domain)

    print("Requesting curl from: %s" % base_url)
    r = requests.get(base_url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'})

    json_result = r.json()

    print(json_result)

    # API Rate limits to 1 second but we are nicer than that
    print('Sleeping for five seconds')
    sleep(5)

    return json_result
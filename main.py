import requests


def max_intelligence_serch(hearo_names, r):

    name_s = str()
    intel = 0

    for sn in hearo_names:
        for x in r:
            if str(sn) == str(x['name']):
                if intel < int(x["powerstats"]["intelligence"]):
                    intel = x["powerstats"]["intelligence"]
                    name_s = x["name"]

    return name_s, intel


if __name__ == '__main__':
    serch_sh = ['Hulk', 'Captain America', 'Thanos']

    u = "https://akabab.github.io/superhero-api/api/all.json"
    req_code = requests.get(u)
    r = requests.get(u).json()
    if 100 < req_code.status_code < 300:
        max_sh, max_int = max_intelligence_serch(serch_sh, r)
        print(f'MAX intelligence of {max_sh} is {max_int}')
    else:
        print('Request error')
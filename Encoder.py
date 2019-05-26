'''
"DBOH" ENCODER ALGORITHM by SD CHOI,
FASTCAMPUS PROGRAMMING SCHOOL APPLICANT (c)
2019.5.26. 
'''

#10진수(소수) -> 2진수 변환

nm = float(input("Num?"))
box = []
fm = nm*2
while fm > 0:
    if fm > 1:
        sm = int(fm)
        box.append(sm)
        fm -= 1
        fm *= 2
        if fm > 1 and nm <= 0.9999:
            break
    elif fm < 1:
        sm = int(fm)
        box.append(sm)
        fm *= 2
    elif fm == 1:
        sm = int(fm)
        box.append(sm)
        break

#10진수 -> 2진수 변환

nm = int(input("Num?"))
box = []

while nm > 1:
    fm = int(nm % 2)
    box.append(fm)
    nm = int(nm / 2)
if nm == 1:
    box.append(nm)

xob = box[::-1]
print(xob)

#10진수 -> 8진수 변환

nm = int(input("Num?"))
box = []

while nm > 1:
    fm = int(nm % 8)
    box.append(fm)
    nm = int(nm / 8)
if nm == 1:
    box.append(nm)

xob = box[::-1]
print(xob)

#10진수 -> 16진수 변환

nm = int(input("Num?"))
box = []

while nm > 1:
    fm = int(nm % 16)
    box.append(fm)
    nm = int(nm / 16)
if nm == 1:
    box.append(nm)

xob = box[::-1]
hset = []

for i in xob:
    if i == 10:
        hset.append("A")
    elif i == 11:
        hset.append("B")
    elif i == 12:
        hset.append("C")
    elif i == 13:
        hset.append("D")
    elif i == 14:
        hset.append("E")
    elif i == 15:
        hset.append("F")
    else:
        hset.append(i)


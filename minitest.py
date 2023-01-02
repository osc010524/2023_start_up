day = int(input("결5석일수를 입력: "))
sc = int(input("점수룰 입력: "))
avg = ""
if day >= 4:
    avg = "F"

else:
    if sc>90:
        avg = "A"
    elif sc<=90 and sc > 80:
        avg = "B"
    elif sc<=80 and sc > 70:
        avg = "C"
    elif sc<=70 and sc > 60:
        avg = "D"
    else:
        avg = "F"

print(avg)
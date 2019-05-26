fcard = ["/1/","/3/","/5/","/7/"]
scard = ["/2/","/3/","/6/","/7/"]
tcard = ["/4/","/5/","/6/","/7/"]
cardrange = list(range(1,8))  # 나올 수 있는 카드 숫자: 1~7

print("SD: Think of an integar among",cardrange)
print(fcard)


firstq = input("SD: Do you see you number here? (y/n):")  #if-else로 총 8가지 경우의 수 생성.
if firstq == "y":      #going for Y<-Y<-Y
    print(scard)
    secondq = input("SD: Do you see you number here? (y/n):")
    if secondq == "y":   #if True(here, y):  참값인 y를 인풋받으면, 다음 실행.
        print(tcard)
        thirdq = input("SD: Do you see you number here? (y/n):")
        if thirdq == "y":
            print("The number is 7.")       # 1. Y<-Y<-Y. 코드블록 유의.
        elif thirdq == "n":
            print("The number is 3.")       # 2. N<-Y<-Y
    elif secondq == "n":
        print(tcard)
        thirdq = input("SD: Do you see you number here? (y/n):")
        if thirdq == "y":
            print("The number is 5.")       # 3. Y<-N<-Y
        elif thirdq == "n":
            print("The number is 1.")       # 4. N<-N<-Y
elif firstq == "n":  #N
    print(scard)
    secondq = input("SD: Do you see you number here? (y/n):")
    if secondq == "y": #Y
        print(tcard)
        thirdq = input("SD: Do you see you number here? (y/n):")
        if thirdq == "y": #Y
            print("The number is 6.") # 5. Y<-Y<-N
        elif thirdq == "n":
            print("The number is 2.")  # 6. N<-Y<-N
    elif secondq == "n":
        print(tcard)
        thirdq = input("SD: Do you see you number here? (y/n):")
        if thirdq == "y":
            print("The number is 4.")  # 7. Y<-N<-N
        elif thirdq == "n":
            print("You are lying.")  # 8. N<-N<-N



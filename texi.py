cash = int(input("돈이 얼마나 있나요? : ")) 
card = input("신용카드가 있나요?(yes/no) : ")
if cash >=4800 :
    print("택시를 타고 가세요.")
else :
    if card == "yes" :
        print("택시를 타고 가세요.")
    elif card == "no":
        print("걸어가세요..")
    else :
        print("돈을 가져오세요 ...")
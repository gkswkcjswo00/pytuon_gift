while True:

    num=input("점수를 입력하세요")
    try:
        num=float(num)
            

        if  num>=0.9:
            print('A')
        elif num>=0.8:
            print('B')
        elif num>=0.7:
            print('C')
        elif num>=0.6:
            print('D')
        elif num>=0:
            print('F')
        else:
            print("0")
    
        
    except:
        print("잘못된 값")

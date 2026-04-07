

def check_num(range_num):
    try:
        num = input("선택 : ")
        num.lstrip() #왼쪽 공백 제거
        num.rstrip() #오른쪽 공백 제거

        num = int(num)
    except ValueError:
        #숫자 변환 실패, ex) 23a
        print("!!!숫자가 아닙니다!!!")
        return 0
    except TypeError:
        #숫자 변환 실패 ex) sdfs
        print("!!!숫자가 아닙니다!!!")
        return 0
    except KeyboardInterrupt:
        #Ctrl + C
        print("!!!Ctrl + C로 종료되지 않습니다!!!")
    else:
        #허용 범위 밖 숫자
        if 0 >= num or num > range_num:
            return 0
        return num
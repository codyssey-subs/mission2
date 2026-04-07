

def check_num(range_num):
    try:
        num = input("선택 : ")
        num.lstrip() #왼쪽 공백 제거
        num.rstrip() #오른쪽 공백 제거

        num = int(num)
    except ValueError:
        #숫자 변환 실패
        print("!!!숫자가 아닙니다.!!!")
        return 0
    except TypeError:
        #숫자 변환 실패
        print("!!!숫자가 아닙니다.!!!")
        return 0
    else:
        if 0 >= num or num > range_num:
            return 0
        return num


def check_num(num, size):
    try:
        num.lstrip() #왼쪽 공백 제거
        num.rstrip() #오른쪽 공백 제거

        num = int(num)
    except:
        #숫자 변환 실패
        return 0
    else:
        return num
#utils.py

import json
from classes.class_quiz import Quiz

def handle_file_exception(e):
    if isinstance(e, FileNotFoundError):
        print("⚠️ 파일이 없어 새로 시작합니다!")
    elif isinstance(e, json.JSONDecodeError):
        print("⚠️ 파일 형식이 잘못되었습니다!")
    elif isinstance(e, PermissionError):
        print("⚠️ 파일 권한이 없습니다!")
    else:
        print(f"⚠️ 파일 오류: {e}")

def check_num(msg, range_num):
    try:
        num = input(msg)
        num.lstrip() #왼쪽 공백 제거
        num.rstrip() #오른쪽 공백 제거
        num = int(num)
    except ValueError:
        #숫자 변환 실패, ex) 23a
        print()
        print("⚠️ 잘못된 입력입니다. 숫자를 입력하세요!")
        return 0
    except TypeError:
        #숫자 변환 실패 ex) sdfs
        print()
        print("⚠️ 잘못된 입력입니다. 숫자를 입력하세요!")
        return 0
    except KeyboardInterrupt:
        #Ctrl + C
        print()
        print("⚠️ 잘못된 입력입니다. Ctrl + C로 종료되지 않습니다!")
        return 0
    except EOFError:
        #Ctrl + D
        print()
        print("⚠️ 잘못된 입력입니다. Ctrl + D로 안전 종료합니다!")
        return 5
    else:
        #허용 범위 밖 숫자
        if 0 >= num or num > range_num:
            print("⚠️ 잘못된 입력입니다. 1~" + str(range_num), "사이의 숫자를 입력해주세요!")
            return 0
        return num

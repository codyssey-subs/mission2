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

# def handle_input_exception(e):
#     if isinstance(e, KeyboardInterrupt):
#         print("\n⚠️ 잘못된 입력입니다. \nCtrl + C로 종료되지 않습니다!")
#     elif isinstance(e, EOFError):
#         print("\n⚠️ 잘못된 입력입니다. \nCtrl + D로 안전 종료합니다!")
#     else:
#         print(f"\n⚠️ 입력 오류: {e}")

def check_num(msg, range_num):
    while True:
        try:
            num = input(msg)
            num.strip() #공백제거
            num = int(num)

            if 1 <= num <= range_num:
                return num

            print(f"⚠️ 잘못된 입력입니다. \n1~" + str(range_num), "사이의 숫자를 입력해주세요!")
        except ValueError:
            #숫자 변환 실패, ex) 23a
            print("\n⚠️ 잘못된 입력입니다. \n숫자를 입력하세요!")
        except TypeError:
            #숫자 변환 실패 ex) sdfs
            print("\n⚠️ 잘못된 입력입니다. \n숫자를 입력하세요!")
        except KeyboardInterrupt:
            #Ctrl + C
            print("\n⚠️ 잘못된 입력입니다. \nCtrl + C로 종료되지 않습니다!")
        except EOFError:
            #Ctrl + D
            print("\n⚠️ 잘못된 입력입니다. \nCtrl + D로 안전 종료합니다!")

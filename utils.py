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
    
def quiz_add_basic(quizGame):
    quizGame.quizzes.append(
        Quiz("세상에서 가장 바쁜 떡은?",
            "가래떡", 
            "백설기", 
            "헐레벌떡", 
            "인절미", 
            3
        )
    )
    quizGame.quizzes.append(
        Quiz("세상에서 가장 뜨거운 바다는?", 
            "동해", 
            "남해", 
            "열받아", 
            "서해",
            3
        )
    )
    quizGame.quizzes.append(
        Quiz("프로그래머가 바다에 가면 먼저 찾는 것은?", 
            "fish", 
            "C", 
            "ship", 
            "sand", 
            2
        )
    )
    quizGame.quizzes.append(
        Quiz("세상에서 가장 쉬운 숫자는?", 
            "0",
            "1",
            "2147483647",
            "190000",
            4
        )
    )
    quizGame.quizzes.append(
        Quiz("세상에서 가장 잔인한 비빔밥은?",
            "불고기 비빔밥",
            "돌솥비빔밥",
            "산채비빔밥",
            "해물비빔밥",
            3
        )
    )
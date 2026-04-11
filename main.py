from utils import check_num
from quiz_add import *
from class_quiz import Quiz
from class_quizgame import QuizGame
from quiz_utils import *

def print_menu():
    print("========================================")
    print("        🎯 나만의 퀴즈 게임 🎯")
    print("========================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("========================================")

def start_quiz(quizGame):
    while True:
        print_menu()
        num = input("선택 : ")
        menu_num = check_num(num, 5)

        if menu_num == 1:
            quiz_play(quizGame)
        elif menu_num == 2:
            print("quiz_add()")
            #quiz_add()
        elif menu_num == 3:
            quiz_list(quizGame)
        elif menu_num == 4:
            print("check_score()")
            #check_score()
        elif menu_num == 5:
            print("exit")
            break
        else: #허용 범위 밖 숫자
            pass

def main():
    quizGame = QuizGame()
    # if : #파일 오픈 실패시
    #     quiz_add_basic(quizGame)
    start_quiz(quizGame)

if __name__ == "__main__":
    main()
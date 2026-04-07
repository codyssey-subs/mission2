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
    return input("선택 : ")

def start_quiz():
    while True:
        menu = int(print_menu())

        if menu == 1:
            #quiz_play()
            print("quiz_play()")
        elif menu == 2:
            print("quiz_add()")
            #quiz_add()
        elif menu == 3:
            print("quiz_list()")
            #quiz_list()
        elif menu == 4:
            print("check_score()")
            #check_score()
        elif menu == 5:
            print("exit")
            break
        else:
            print()
            print("!!!1 ~ 5 사이의 숫자를 입력해주세요!!!!")
            print()

def main():
    start_quiz()

if __name__ == "__main__":
    main()
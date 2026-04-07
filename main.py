from utils import check_num

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

def start_quiz():
    while True:
        print_menu()
        range_num = 5
        menu_num = check_num(range_num)

        if menu_num == 1:
            #quiz_play()
            print("quiz_play()")
        elif menu_num == 2:
            print("quiz_add()")
            #quiz_add()
        elif menu_num == 3:
            print("quiz_list()")
            #quiz_list()
        elif menu_num == 4:
            print("check_score()")
            #check_score()
        elif menu_num == 5:
            print("exit")
            break
        else: #허용 범위 밖 숫자
            print("!!!1 ~", range_num, "사이의 숫자를 입력해주세요!!!!")
            print()

def main():
    start_quiz()

if __name__ == "__main__":
    main()
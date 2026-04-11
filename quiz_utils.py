#quiz_utils.py

from utils import *
from class_quiz import *

def quiz_play(quizGame):
    #퀴즈가 없는 경우
    if len(quizGame.quizzes) == 0:
        print("!!!퀴즈가 없습니다. 퀴즈를 추가해주세요!!!")
        return
    #퀴즈가 있는 경우
    score = 0
    for q in quizGame.quizzes:
        print("[문제]")
        print(q.question + '?')
        for choice in q.choices:
            print(choice)
        answer = check_num("정답: ", 4) #정답 입력
        if answer == q.answer: #정답/오답 여부
            print("✅ 정답입니다!")
            score += 1
        else:
            print("❌ 오답입니다!")
    print("========================================") #결과 표시
    print("🏆 결과: " + str(score) + "문제 중 " + str(quizGame.cnt) + "문제 정답!")
    if quizGame.best_score < score / quiaGame.cnt:
        print("🎉 새로운 최고 점수입니다!")
    print("========================================")


def quiz_list(quizGame):
    #퀴즈가 없는 경우
    if len(quizGame.quizzes) == 0:
        print("⚠️ 퀴즈가 없습니다. 퀴즈를 추가해주세요!")
        return
    #퀴즈가 있는 경우
    print()
    print("📋 등록된 퀴즈 목록 (총 " + str(len(quizGame.quizzes)) + "개)")
    for q in quizGame.quizzes:
        q.print_quiz()
        
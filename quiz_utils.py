#quiz_utils.py

from utils import *
from class_quiz import *

def quiz_play(quizGame):
    #퀴즈가 없는 경우
    if len(quizGame.quizzes) == 0:
        print("⚠️ 퀴즈가 없습니다. 퀴즈를 추가해주세요!")
        return
    #퀴즈가 있는 경우
    score = 0
    print()
    for q in quizGame.quizzes:
        print("[문제]")
        print(q.question)
        for i in range(4):
            print(f"[{i + 1}] {q.choices[i]}")
        answer = check_num("정답: ", 4) #정답 입력
        if answer == q.answer: #정답/오답 여부
            print("✅ 정답입니다!\n")
            score += 1
        else:
            print("❌ 오답입니다!\n")
    print("========================================") #결과 표시
    print(f"🏆 결과: {len(quizGame.quizzes)}문제 중 {score}문제 정답!")
    if quizGame.best_score < (score / len(quizGame.quizzes)):
        quizGame.best_score = (score / len(quizGame.quizzes))
        print("🎉 새로운 최고 점수입니다!")
    print("========================================\n")


def quiz_list(quizGame):
    #퀴즈가 없는 경우
    if len(quizGame.quizzes) == 0:
        print("⚠️ 퀴즈가 없습니다. 퀴즈를 추가해주세요!")
        return
    #퀴즈가 있는 경우
    print()
    print(f"📋 등록된 퀴즈 목록 (총 {len(quizGame.quizzes)}개)\n")
    for q in quizGame.quizzes:
        q.print_quiz()
        
def quiz_play(quizGame):
    #퀴즈가 없는 경우
    if len(quizGame.quizzes) == 0:
        print("!!!퀴즈가 없습니다. 퀴즈를 추가해주세요!!!")
        return
    #퀴즈가 있는 경우
    score = 0
    for q in quizGame.quizzes:
        print(q["question"])
        for choice in q["choices"]:
            print(choice)
        answer = int(input("정답: ")) #정답 입력
        if answer == q["answer"]: #정답/오답 여부
            print("!!!정답입니다!!!")
            score += 1
        else:
            print("!!!오답입니다!!!")
    print(str(score) + " / " + str(quizGame.cnt)) #결과 표시

def quiz_list(quizGame):
    #퀴즈가 없는 경우
    if len(quizGame.quizzes) == 0:
        print("!!!퀴즈가 없습니다. 퀴즈를 추가해주세요!!!")
        return
    #퀴즈가 있는 경우
    for q in quizGame.quizzes:
        print(q)
def quiz_list(quizGame):
    #퀴즈가 없는 경우
    if len(quizGame.quizzes) == 0:
        print("!!!퀴즈가 없습니다. 퀴즈를 추가해주세요!!!")
        return
    for q in quizGame.quizzes:
        print(q)
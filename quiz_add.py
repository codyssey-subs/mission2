from class_quiz import *

def quiz_add_basic():
    quizGame.quizzes.append(
        Quiz("세상에서 가장 바쁜 떡은?",
            "가래떡", 
            "백설기", 
            "헐레벌떡", 
            "인절미", 
            4
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
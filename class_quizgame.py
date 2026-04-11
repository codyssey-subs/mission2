#class_quizgame.py

import json
from class_quiz import *

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0 #최고 점수
    #
    #메뉴표시
    #
    #퀴즈 풀기
    #
    #퀴즈 추가
    #
    #목록 보기
    #
    #점수 확인
    #
    #파일 저장
    def save_data(self):
        try:
            state = {
                "quizzes": [quiz.to_dict() for quiz in self.quizzes],
                "best_score": self.best_score
            }
            with open("state.json", "w", encoding="utf-8") as f:
                json.dump(state, f, ensure_ascii=False, indent =4)
        except FileNotFoundError:
            print("파일이 없어 새로 시작합니다.")
        except json.JSONDecodeError:
            print("파일 형식이 잘못되었습니다.")
        except PermissionError:
            print("파일 권한이 없습니다.")
        except OSError as e:
            print(f"파일 오류: {e}")
    #파일 불러오기
    def load_data(self):
        try:
            with open("state.json", "r", encoding="utf-8") as f:
                state = json.load(f)
            self.quizzes = [
                Quiz(q["question"], q["choices"][0], q["choices"][1], q["choices"][2], q["choices"][3], q["answer"])
                for q in state["quizzes"]
            ]
        except FileNotFoundError: #파일 불러오기 실패 시 기본 데이터 사용
            #quiz_add_basic()
            print("파일이 없어 새로 시작합니다.")
        except json.JSONDecodeError:
            print("파일 형식이 잘못되었습니다.")
        except PermissionError:
            print("파일 권한이 없습니다.")
        except OSError as e:
            print(f"파일 오류: {e}")
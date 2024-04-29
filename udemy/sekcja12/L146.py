import requests
import html


class Question:
    def __init__(self, category, questionStr, correctAnswerFlag):
        self.category = category
        self.questionStr = questionStr
        self.correctAnswerFlag = correctAnswerFlag


class Quiz:
    def __init__(self, numQuestions):
        self.apiUrl = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount="
        self.numQuestions = numQuestions
        self.questtionsList = []
        self.loadQuestions(numQuestions)

    def loadQuestions(self, numQuestions):
        response = requests.get(self.apiUrl + str(numQuestions))
        #{'response_code': 0, 'results': [{'category': 'History', 'type': 'boolean', 'difficulty': 'easy', 'question': 'The Cold War ended with Joseph Stalin&#039;s death.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'category': 'Entertainment: Film', 'type': 'boolean', 'difficulty': 'easy', 'question': 'The word &quot;Inception&quot; came from the 2010 blockbuster hit &quot;Inception&quot;.', 'correct_answer': 'False', 'incorrect_answers': ['True']},
        if response.ok :
            #print(response.json())
            data = response.json()
            results = data["results"]

            for q in results:
                category = q["category"]
                questionType = q["type"]
                difficulty = q["difficulty"]
                questionStr = html.unescape( q["question"] )
                print(questionStr)
                correctAnswerFlag = q["correct_answer"].lower() in ['true', '1', 'yes']

                qObj = Question(category, questionStr, correctAnswerFlag)
                self.questtionsList.append(qObj)

    def startQuiz(self):
        print("\nWelcome in Quiz!")
        numCorrectUserAnswers = 0
        n = 0
        numQuestions = len(self.questtionsList)

        while( n < numQuestions):
            q = self.questtionsList[n]
            print("Question number " + str(n) + ": ", q.questionStr)
            #print("Answer flag: ", q.correctAnswerFlag)

            answer = input("Give correct answer as y/n:")
            answerBool = False
            if answer == "y": answerBool = True

            if answerBool == q.correctAnswerFlag:
                print("Correct!")
                numCorrectUserAnswers += 1
            else:
                print("Not correct!")

            n += 1

        print("Number of correct answers: ", numCorrectUserAnswers,
                " from ", len(self.questtionsList), " questions")




quiz = Quiz(10)
quiz.startQuiz()

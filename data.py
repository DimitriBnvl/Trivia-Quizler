import requests

#Feel free to tweak the parameters!
#I would recommend keeping the type 'boolean,' but construct shorter or longer quizzes in different categories.
#Notes: category: 18 results in CS related questions.
parameters = {
    "amount" : 10,
    "type" : "boolean",
    "category": 18
}

#Requesting data from Trivia Database API.
response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
response.raise_for_status()

question_data = response.json()["results"]
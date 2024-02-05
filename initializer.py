#Python code for creating a basic chatbot template:

# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

CORPUS_FILE = "_chat.txt"

chatbot = ChatBot("Buddy")
trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)
trainer.train([
    "Hi",
    "Welcome",
])
trainer.train([
    "Are you alive?",
    "No, I'm a robot",
])
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f" {chatbot.get_response(query)}")

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot(
    'BankBuddy',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
)

# Training with Personal Ques & Ans
conversation = [
    "Hello",
    "Hi there!",
    "How can i help?",
    "I want to open a new account",
    "Thank you for your interest sir but you have to visit nearest branch of our bank for account opening.",
    "Okay",
    "Anything else you need help with ?",
    "No. Thank you for your help.",
    "Have a good day, Sir."
    "No. Bye",
    "Bye"
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

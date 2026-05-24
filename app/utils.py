import os

# Load personal information from the text file
with open("some_information.txt", "r", encoding="utf-8") as file:
    personal_info = file.read()

# Function to check if the user's question is relevant
def is_relevant(question, info):
    question_words = set(question.lower().split())
    info_words = set(info.lower().split())

    # Simple keyword overlap check (can be improved with NLP)
    common_words = question_words.intersection(info_words)

    return len(common_words) > 0  # Returns True if there is an overlap
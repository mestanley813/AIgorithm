from dotenv import load_dotenv
import os
import openai

load_dotenv()

class GPT(object):
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_KEY")
        openai.organization = os.getenv("OPENAI_ORGANIZATION")

    def Recommend(self):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Write just the stock ticker you recommend:",
        max_tokens=4,
        temperature=0.7
        )
        response = response["choices"][0]["text"].strip()
        return response
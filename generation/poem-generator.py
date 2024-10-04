
from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
from typing import List
import random
import json
import random

def get_promt( poems: List, num_of_examples:int = 5,):
    start = "The poems bellow are some examples by Lord Byron.\n\n\n"
    mid = []

    for i in range(num_of_examples):
        mid.append(f"Example {i+1}:\n{random.choice(poems)['lines']}\n\n\n")
    end = "Now, write a new poem in the style of Lord Byron. Write only the poem, without title or any explanation.\n\n\n"
    return start + "".join(mid) + end


if __name__ == "__main__":
    with open("data/byron_processed_poems.json", "r", encoding='utf-8') as f:
        poems = json.load(f)

    model = OllamaLLM(model="llama3:8b")

    responses = []
    for _ in range(10):
        print(f"Generating Poem {_+1}")
        response = model.invoke(get_promt(poems))
        responses.append(response)

    with open("./byron_generated_poems.json", "w") as f:
        json.dump(responses, f)



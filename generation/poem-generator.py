from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM


# Define a few-shot prompt template for Lord Byron’s style
byron_prompt = """
Below are poems written in the style of Lord Byron:

Example 1:
{example_1}

Example 2:
{example_2}

Now, write a new poem in the style of Lord Byron:
"""

# Substitute this with actual poems
#TODO: Replace the hardcoded poems from a file, and sample 2-5 poems
poem_1 = """She walks in beauty, like the night
Of cloudless climes and starry skies;
And all that's best of dark and bright
Meet in her aspect and her eyes."""

poem_2 = """When we two parted
In silence and tears,
Half broken-hearted
To sever for years,
Pale grew thy cheek and cold,
Colder thy kiss;"""

# Initialize the PromptTemplate in Langchain
prompt_template = PromptTemplate(
    input_variables=["example_1", "example_2"],
    template=byron_prompt
)

# Format the prompt with Byron examples
formatted_prompt = prompt_template.format(example_1=poem_1, example_2=poem_2)
# print(formatted_prompt)

model = OllamaLLM(model="llama3:8b")
response = model.invoke(formatted_prompt)

print(response)
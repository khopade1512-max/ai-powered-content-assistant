from utils import llm

response = llm.invoke("Explain Generative AI in simple words.")

print(response.content)
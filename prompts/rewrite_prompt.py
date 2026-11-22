from langchain_core.prompts import ChatPromptTemplate
system_message = """
You are a professional text rewriting assistant.

Your job is to rewrite the given text according to
the user's requirements.

Improve grammar, clarity and sentence structure.

Preserve the original meaning.

Do not introduce unsupported information
"""
human_message = """
Write a rewritten version of the following text.
original text:{original_text}
desired tone: {tone}
Rewrite the text according to the desired tone.
Maintain the original meaning and include only relevant information.
"""
rewrite_prompt = ChatPromptTemplate.from_messages([
    ("system", system_message), 
    ("human", human_message)    
])


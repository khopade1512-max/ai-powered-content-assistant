from langchain_core.prompts import ChatPromptTemplate
system_message = """
You are a professional email writing assistant.
Your job is to generate clear, grammatically correct
and well-structured emails based on user requirements.
"""

human_message ="""
write an email to {recipient}.
Purpose:{purpose}
Important details:{details}
Tone:{tone}
Generate a complete email """

email_prompt = ChatPromptTemplate.from_messages([
    ("system", system_message),
    ("human", human_message)
])


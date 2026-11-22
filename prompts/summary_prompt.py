from langchain_core.prompts import ChatPromptTemplate
system_message = """
You are a professional text summarization assistant.

Your job is to summarize lengthy text into clear,
concise and meaningful summaries.

Focus on the important information and preserve
the original meaning of the text.

Do not introduce information that is not present
in the original text.
"""
human_message = """
Summarize the following text.

Text:
{text}

Summary Length: {summary_length}

Generate a summary according to the requested length.
Maintain the original meaning and include only relevant information.
"""
summary_prompt= ChatPromptTemplate.from_messages([
    ("system", system_message), 
    ("human", human_message)    
])

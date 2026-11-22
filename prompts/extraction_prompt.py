from langchain_core.prompts import ChatPromptTemplate
system_message = """You are a professional information extraction assistant.

Your job is to extract relevant information from unstructured text and convert it into a predefined structured format.

Follow the output structure and field definitions provided in the instructions.

Extract only information explicitly available in the input text.

Do not introduce assumptions or additional information.

If any required information is missing, represent it as null.

Preserve the original meaning of the extracted information. """

human_message="""
Extract the following information from the text below and format it according to the specified output structure.
Text: {text}

Required fields:
- name
- age
- profession
- company
- experience"""

extraction_prompt= ChatPromptTemplate.from_messages([
    ("system", system_message), 
    ("human", human_message)    
])
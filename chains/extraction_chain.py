from prompts.extraction_prompt import extraction_prompt
from utils import llm
from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    name:Optional[str]=Field(None, description="The name of the employee")
    age:Optional[int]=Field(None, description="The age of the employee")
    profession:Optional[str]=Field(None, description="The profession of the employee")
    company:Optional[str]=Field(None, description="The company of the employee")
    experience:Optional[int]=Field(None, description="The experience of the employee")

structured_llm=llm.with_structured_output(Employee)
extraction_chain=extraction_prompt|structured_llm

def extract_employee_info(text):
    if not text.strip():
        raise ValueError("Input text cannot be empty.")
    try:
        response = extraction_chain.invoke({"text": text})
    except Exception as e:
        raise RuntimeError(f"Error extracting employee information: {e}") from e 
    return response       
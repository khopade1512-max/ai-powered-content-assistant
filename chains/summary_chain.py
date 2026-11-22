from prompts.summary_prompt import summary_prompt
from utils import llm

summary_chain = summary_prompt | llm

def generate_summary(text, summary_length):
    if not text.strip():
        raise ValueError("Text cannot be empty.")
    if not summary_length.strip():
        raise ValueError("Summary length cannot be empty.")
    try:
        response = summary_chain.invoke({
          "text": text,
          "summary_length": summary_length
        })
    except Exception as e:
        raise RuntimeError(f"Error generating summary: {e}") from e
    return response.content

    
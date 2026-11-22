from prompts.rewrite_prompt import rewrite_prompt
from utils import llm

rewrite_chain = rewrite_prompt | llm

def generate_rewrite(original_text, tone):
    if not original_text.strip():
        raise ValueError("Original text cannot be empty.")
    valid_tones = ["Professional", "Friendly", "Formal", "Casual"]
    tone = tone.strip().capitalize()
    if tone not in valid_tones:
        raise ValueError("Invalid tone. Please choose from: Professional, Friendly, Formal, Casual.")

    try:
        response = rewrite_chain.invoke({
          "original_text": original_text,
          "tone": tone
        })
    except Exception as e:
        raise RuntimeError(f"Error generating rewrite: {e}") from e

    return response.content


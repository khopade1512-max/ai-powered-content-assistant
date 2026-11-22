from prompts.email_prompt import email_prompt
from utils import llm

email_chain = email_prompt | llm

def generate_email(recipient,purpose,details,tone):
    if not recipient.strip():
        raise ValueError("Recipient cannot be empty.")
    if not purpose.strip():
        raise ValueError("Purpose cannot be empty.")
    if not details.strip():
        raise ValueError("Details cannot be empty.")
    valid_tones = ["Professional", "Friendly", "Formal", "Casual"]
    tone = tone.strip().capitalize()
    if tone not in valid_tones:
        raise ValueError(f"Tone must be one of {valid_tones}.")
    try:    
        response = email_chain.invoke({
         "recipient": recipient,
         "purpose": purpose,
         "details": details,
         "tone": tone
       })
    except Exception as e:
        raise RuntimeError(f"Error generating email: {e}") from e

    return response.content


# AI-Powered Content Assistant

## Project Overview

AI-Powered Content Assistant is a Generative AI application built using Python, LangChain, OpenAI, and Streamlit.

The application provides four functionalities:

- **Email Generation:** Generates emails based on recipient, purpose, important details, and tone.
- **Text Summarization:** Summarizes lengthy text into concise and meaningful summaries.
- **Text Rewriting:** Rewrites existing text in different tones.
- **Information Extraction:** Extracts structured employee information from unstructured text using Pydantic.

The project demonstrates the practical implementation of Large Language Models (LLMs), prompt engineering, LangChain chains, structured output, and Streamlit.
## Features

### 1. Email Generation
- Generates emails based on user-provided inputs.
- Supports Professional, Friendly, Formal, and Casual tones.
- Uses customized prompts to generate relevant email content.

### 2. Text Summarization
- Summarizes lengthy text into Short, Medium, and Long formats.
- Preserves important information and original meaning.

### 3. Text Rewriting
- Rewrites existing text according to the selected tone.
- Supports Professional, Friendly, Formal, and Casual tones.

### 4. Information Extraction
- Extracts employee details from unstructured text.
- Uses Pydantic models for structured output.
- Handles missing information using optional fields.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | Building LLM-powered chains and managing prompts |
| OpenAI API | Generating AI responses |
| Streamlit | Building the interactive web application |
| Pydantic | Validating and structuring extracted information |
| Python-dotenv | Managing environment variables securely |
| Git & GitHub | Version control and project hosting |

## Project Structure

ai-powered-content-assistant/
│
├── chains/
│   ├── email_chain.py
│   ├── summary_chain.py
│   ├── rewrite_chain.py
│   └── extraction_chain.py
│
├── prompts/
│   ├── email_prompt.py
│   ├── summary_prompt.py
│   ├── rewrite_prompt.py
│   └── extraction_prompt.py
│
├── app.py
├── utils.py
├── test_chains.py
├── requirements.txt
├── .gitignore
└── README.md

## Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

git clone https://github.com/khopade1512-max/ai-powered-content-assistant.git


### 2. Navigate to the Project Directory

cd ai-powered-content-assistant

### 3. Create a Virtual Environment

```bash
python -m venv myenv
```

### 4. Activate the Virtual Environment

For Windows:

myenv\Scripts\activate

For macOS/Linux:

source myenv/bin/activate


### 5. Install Dependencies


pip install -r requirements.txt


### 6. Configure the OpenAI API Key

Create a `.env` file in the project root directory.

Add your API key:
OPENAI_API_KEY=your_api_key_here


Replace `your_api_key_here` with your actual OpenAI API key.

**Note:** Never upload your `.env` file or expose your API key publicly.

## How to Run the Application

After completing the installation and configuration steps, run the following command:


python -m streamlit run app.py


The application will open in your default web browser.

You can select any of the four functionalities from the sidebar:

- Email Generation
- Text Summarization
- Text Rewriting
- Information Extraction

## Future Improvements

- Add conversation history.
- Improve error handling and user experience.
- Add support for additional document formats.
- Implement more advanced prompt engineering techniques.
- Deploy the application online.
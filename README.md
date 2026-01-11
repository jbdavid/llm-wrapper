# LLM Wrapper

## Project Purpose
This project is a REST API built with FastAPI that analyzes customer questions using language models (LLMs) like OpenAI GPT-4 or Google Gemini. The API takes a question as input and returns a structured analysis (mood, priority, tags).

## Tech Stack
- **Language** : Python 3.13
- **Framework** : FastAPI (asynchronous web server)
- **LLMs** : Integration with LangChain for OpenAI and Google Gemini
- **Validation** : Pydantic for data models
- **Dependency Management** : uv (replaces pip and virtualenv)
- **Environment Variables** : python-dotenv

## Prerequisites
- Python 3.13 (managed by uv)
- API keys for OpenAI and/or Google Gemini

## Installation
1. **Clone the repository** :
   ```bash
   git clone <repo-url>
   cd llmwrapper
   ```

2. **Install uv** (if not already done) :
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Install dependencies** :
   ```bash
   uv sync
   ```

## Environment Variables Configuration
Create a `.env` file at the project root with the following variables :

```env
# OpenAI API Key (required if PROVIDER=openai)
OPENAI_API_KEY=your_openai_key_here

# Google API Key (required if PROVIDER=gemini)
GOOGLE_API_KEY=your_google_key_here

# Provider to use: 'openai' or 'gemini'
PROVIDER=gemini
```

- **OPENAI_API_KEY** : Get it from [platform.openai.com](https://platform.openai.com/api-keys).
- **GOOGLE_API_KEY** : Get it from [Google AI Studio](https://aistudio.google.com).
- **PROVIDER** : Choose `openai` for GPT-4 or `gemini` for Gemini 1.5 Pro.

## Running the Project
1. **Make the script executable** (if needed) :
   ```bash
   chmod +x run.sh
   ```

2. **Launch the application** :
   ```bash
   ./run.sh
   ```

   This activates the virtual environment and starts the FastAPI server in development mode on `http://127.0.0.1:8000`.

## API Usage
- **Documentation** : Visit `http://127.0.0.1:8000/docs` for the Swagger interface.
- **Main Endpoint** : `POST /ask`
  - Request Body : `{"question": "Your customer question"}`
  - Response : Structured analysis (mood, priority, tags)

Example with curl :
```bash
curl -X POST "http://127.0.0.1:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "My product arrived broken"}'
```

## Project Structure
- `main.py` : FastAPI entry point
- `models/` : Pydantic data models
- `app/` : (if applicable) Additional logic
- `.env` : Environment variables (not committed)
- `run.sh` : Launch script

## Development
- To add a new LLM provider, modify the `get_model()` function in `main.py`.
- Dependencies are managed in `pyproject.toml`.

## License
[Add your license here]
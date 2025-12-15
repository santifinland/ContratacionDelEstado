# Contratacion Del Estado
IA Agent for Spanish Contratacion Del Estado platform

## 🐍 Virtual environment & dependencies

Create and activate a Python virtual environment and install the required dependencies.

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment (Linux / macOS)
source venv/bin/activate

# Activate virtual environment (Windows PowerShell)
# venv\Scripts\Activate.ps1

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install --pre -U langfuse langchain-openai python-dotenv
```


## 🔐 Environment variables (LangSmith & OpenAI)

This project uses environment variables to configure and OpenAI access
and Langfuse tracing.
Environment variables are loaded from a `.env` file using `python-dotenv`.


### Setup

```bash
# Create .env file
touch .env
cat <<EOF >> .env

MG_MODEL=<your-openai-model>
MG_BASE_URL=<your-openai-model-gateway>
MG_API_KEY=<your-open-ai-model-gateway-api-key>
USER=<your-openai-model-gateway-user>

LANGFUSE_SECRET_KEY=<your-langfuse-secret-key>
LANGFUSE_PUBLIC_KEY=<your-langfuse-public-key>
LANGFUSE_BASE_URL=<your-languse-instance-url>
EOF
```

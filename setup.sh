#!/bin/bash
set -e

echo "🚀 Setting up Synapse-Code Environment..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Setup .env if it doesn't exist
if [ ! -f .env ]; then
    cp .env.example .env
    echo "⚠️ .env created. Please add your OPENAI_API_KEY to .env"
fi

echo "✅ Setup complete. Start the server with: source venv/bin/activate && uvicorn app.main:app --reload"

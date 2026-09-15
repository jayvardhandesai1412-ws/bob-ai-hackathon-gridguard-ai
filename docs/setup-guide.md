# Setup Guide

## Prerequisites

- Python 3.10+
- Node.js 18+
- Git
- IBM Bob

## Installation

### Clone the repository

git clone https://github.com/jayvardhandesai1412-ws/bob-ai-hackathon-gridguard-ai.git

### Backend

cd src/backend
pip install -r requirements.txt
python app.py

### Frontend

cd ../frontend
npm install
npm start

## Environment Variables

No external API keys are required for the demo.

## Verify

Open http://localhost:3000 and confirm the dashboard loads.

## Troubleshooting

- `ModuleNotFoundError` → Run `pip install -r requirements.txt`
- `npm not found` → Install Node.js

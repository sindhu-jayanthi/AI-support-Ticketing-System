AI Support Ticket Management System

An AI-powered support ticket management system built using FastAPI, Python, PostgreSQL, SQLAlchemy and Google Gemini.

The application allows users to create and manage support tickets while automatically classifying ticket categories and analyzing customer sentiment using Gemini AI.

Features

Ticket Management: Create, retrieve, update and delete support tickets.

AI Ticket Classification: Automatically categorizes tickets into Payment Issue, Technical Issue, Account Access and General Inquiry.

Sentiment Analysis: Identifies customer sentiment as Positive, Negative or Neutral.

PostgreSQL Integration: Stores ticket information persistently using SQLAlchemy ORM.

Asynchronous Operations: Uses async FastAPI endpoints and SQLAlchemy sessions.

Ticket Filtering: Filter tickets based on their status.

Pagination & Sorting: Retrieve records in manageable batches with configurable sorting.

Pydantic Validation: Validates incoming requests and structures API responses.

Tech Stack

Python

FastAPI

PostgreSQL

SQLAlchemy (Async)

Pydantic

Google Gemini API

Uvicorn

Project Structure

AI_Support_Ticket_System/
│
├── main.py
├── models.py
├── database.py
├── database_models.py
├── gemini_service.py
├── requirements.txt
├── .env
└── .gitignore

Setup Instructions

1. Clone the repository

git clone YOUR_REPOSITORY_URL
cd AI_Support_Ticket_System

2. Create and activate a virtual environment

python -m venv .venv

Windows:

.venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Configure environment variables

Create a .env file:

DATABASE_URL=postgresql+asyncpg://postgres:YOUR_PASSWORD@localhost:5432/support_ticket_db
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

Replace the placeholders with your PostgreSQL credentials and Gemini API key.

5. Run the application

uvicorn main:app --reload

6. Access API documentation

Open:

http://127.0.0.1:8000/docs

AI Capabilities

Google Gemini is integrated to:

Classify incoming support tickets automatically.

Analyze customer sentiment.

Generate structured AI insights from customer descriptions.

Future Enhancements

AI-generated customer response suggestions.

Ticket prioritization based on sentiment.

Customer and support-agent management.

Dashboard and analytics.

Improved AI error handling.

Security

Store API keys and database credentials in environment variables.

Never commit .env to GitHub.

Use .gitignore to exclude sensitive configuration files.

Project Status: Backend CRUD and initial Gemini AI integration implemented.

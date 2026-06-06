# 📚 CrispDeck

CrispDeck is an AI-powered study deck generation platform that transforms PDFs, PPTX presentations, and DOCX documents into Anki-compatible flashcard decks.

The platform uses an agentic workflow to extract content, analyze syllabus coverage, identify key concepts, generate flashcards, validate them, and export them as APKG files for Anki.

---

## 🚀 Features

* PDF Processing
* PPTX Processing
* DOCX Processing
* Multi-file Upload Support
* AI-Powered Concept Extraction
* Syllabus Coverage Analysis
* Flashcard Generation
* Flashcard Validation
* CSV Export
* APKG Export
* OpenRouter LLM Integration
* Streamlit Web Interface

---

## 🧠 Agent Workflow

Document Upload

↓

Extraction Agent

↓

Coverage Agent

↓

Concept Agent

↓

Generation Agent

↓

Validation Agent

↓

CSV / APKG Export

---

## 📊 Coverage Analysis

Users can upload a syllabus along with study material.

CrispDeck analyzes the uploaded resources and identifies:

* Covered Topics
* Partially Covered Topics
* Missing Topics

This helps students identify knowledge gaps before exams.

---

## 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI

* OpenRouter
* GPT OSS Models

### Document Processing

* PyMuPDF
* python-pptx
* python-docx

### Deck Generation

* Genanki

---

## 📂 Supported File Types

| Type | Supported |
| ---- | --------- |
| PDF  | ✅         |
| PPTX | ✅         |
| DOCX | ✅         |

---

## ⚡ Local Setup

Clone Repository

git clone https://github.com/RandomJainam/CrispDeck.git

cd CrispDeck

Install Dependencies

pip install -r requirements.txt

Create .env

OPENROUTER_API_KEY=your_key_here

Run

streamlit run app.py

---

## 🔮 Future Roadmap

* Diagram/Image Understanding
* Coverage Analysis V2
* Telegram Bot Integration
* User Authentication
* Deck History
* Cloud Storage
* Advanced Study Analytics

---

## 👨‍💻 Author

Jainam Gada

Information Technology Student

Building AI-powered educational tools and automation systems.

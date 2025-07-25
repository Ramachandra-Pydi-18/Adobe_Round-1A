# Connecting the Dots - Round 1A: PDF Outline Extractor

# Adobe Round 1A - Entity & Relationship Extraction

This project solves the Adobe Round 1A challenge which involves extracting key entities and their relationships from structured/unstructured textual data. The aim is to build a basic NLP pipeline to identify entities such as `Person`, `Organization`, `Location`, and their interactions in text.

---

## 📂 Project Structure

round1a-entity-extraction/
├── input/ # Folder with input text files
├── output/ # Folder where extracted JSONs will be saved
├── src/
│ ├── main.py # Entry-point to the pipeline
│ ├── extractor.py # Entity and relationship extraction logic
│ ├── preprocessor.py # Text cleaning and tokenization
│ └── utils.py # Helper utilities
├── requirements.txt # Python dependencies
├── approach_explanation.md# Brief explanation of the approach
└── README.md # This file



---

## 📌 Problem Statement

Given a set of textual inputs, extract and classify entities and map relationships among them. Your output should be a structured JSON containing:

- Identified Entities (Name, Type)
- Relationships (Subject, Predicate, Object)

---

## 🧠 Approach

1. **Preprocessing**: Normalize, clean, and tokenize the input text.
2. **NER (Named Entity Recognition)**: Identify entities using spaCy or rule-based methods.
3. **Relationship Extraction**: Use syntactic patterns and dependency parsing to identify relations.
4. **Output Generation**: Format the output in structured JSON.

> Detailed explanation can be found in `approach_explanation.md`.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Ramachandra-Pydi-18/Adobe-round-1a.git
cd Adobe-round-1a
2. Create and Activate Virtual Environment

python -m venv venv
For Windows:


venv\Scripts\activate
For Unix/Mac:

source venv/bin/activate
3. Install Dependencies

pip install -r requirements.txt
🚀 Run the Project
Place your input text files in the input/ folder, then run:

python src/main.py
📤 Output
The output will be stored in the output/ directory as structured JSON files:


{
  "entities": [
    { "name": "Ram", "type": "Person" },
    { "name": "Adobe", "type": "Organization" }
  ],
  "relationships": [
    { "subject": "Ram", "predicate": "works at", "object": "Adobe" }
  ]
}
📚 Requirements
Python 3.8+

spaCy

re, os, json

tqdm

nltk (optional)

Install missing packages with:

pip install spacy tqdm nltk
To download the English NLP model for spaCy:

python -m spacy download en_core_web_sm
🤝 Contribution
Developed by Ramachandra Pydi as part of the Adobe Round 1A Machine Learning Challenge.

Feel free to fork, raise issues, or contribute!

📬 Contact
📧 Email: ramachandrapydi18@gmail.com
🌐 GitHub: Ramachandra-Pydi-18


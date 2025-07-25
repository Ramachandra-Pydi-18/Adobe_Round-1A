# Connecting the Dots - Round 1A: PDF Outline Extractor

## Description
Extracts structured outline (Title, H1, H2, H3) from PDFs.

## Tech Stack
- Python 3.10
- PyMuPDF (fitz)
- Docker

## Build Docker Image
```bash
docker build --platform linux/amd64 -t pdf-parser:<your_id> .
# PDF Outline Extractor using Docker 🐳

This project extracts the outline (bookmarks) from a PDF file using Python and runs inside a Docker container.

## 💻 How to Use

1. Place the `.pdf` file inside the `input/` folder.
2. Build the Docker image:
   ```bash
   docker build -t pdf-parser:test123 .

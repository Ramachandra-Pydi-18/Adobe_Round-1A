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

# 📄 RAG Tutorial 01 — Document Loading & Parsing

<p align="center">
  <a href="https://github.com/kishore2797/mastering-rag"><img src="https://img.shields.io/badge/Series-Mastering_RAG-blue?style=for-the-badge" /></a>
  <img src="https://img.shields.io/badge/Part-1_of_16-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Difficulty-Beginner-brightgreen?style=for-the-badge" />
</p>

> **Part of the [Mastering RAG](https://github.com/kishore2797/mastering-rag) tutorial series**  
> Previous: — | Next: [02 — Chunking Strategies](https://github.com/kishore2797/rag-02-chunking-strategies)

---

## 🌍 Real-World Scenario

> Imagine you're building a **legal contract analyzer** for a law firm. Lawyers upload hundreds of contracts (PDFs, Word docs) and need to search them. Before any AI magic can happen, you need to reliably extract clean text from every file format — handling scanned PDFs, weird DOCX formatting, and corrupted files gracefully. That's this tutorial.

---

## 🏗️ What You'll Build

A full-stack document ingestion and parsing system that accepts **PDF, DOCX, TXT, and Markdown** files through a unified API. Each format is handled by a dedicated parser that extracts clean, structured text — ready for chunking, embedding, and retrieval in downstream RAG pipelines.

```
Upload: resume.pdf, contract.docx, notes.txt, guide.md
  ↓
API: POST /api/documents/upload
  ↓
Output: { text: "...", metadata: { source, pages, format, size, ... } }
```

## 🔑 Key Concepts

- **Document loaders**: format-specific parsers (PyPDF2 for PDF, python-docx for DOCX, etc.)
- **Metadata extraction**: page numbers, headings, file info, word count
- **Text cleaning**: normalize whitespace, handle encoding, strip artifacts
- **Unified API**: one endpoint accepts any supported format
- **Error handling**: graceful handling of corrupted files, unsupported formats

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11+ · FastAPI · PyPDF2 · python-docx · markdown |
| Frontend | React 19 · Vite · Tailwind CSS |

## 📁 Project Structure

```
rag-01-document-loading/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI application
│   │   ├── parsers/
│   │   │   ├── pdf_parser.py    # PDF extraction
│   │   │   ├── docx_parser.py   # DOCX extraction
│   │   │   ├── txt_parser.py    # Plain text handling
│   │   │   └── md_parser.py     # Markdown parsing
│   │   ├── models/              # Pydantic schemas
│   │   └── api/                 # Route handlers
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── components/
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## 🚀 Quick Start

### Backend

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 — upload documents and see parsed output.

## 📖 What You'll Learn

1. How different document formats store text internally
2. Why metadata preservation matters for RAG
3. How to build a unified ingestion API that handles any format
4. Common pitfalls: encoding issues, scanned PDFs, corrupted files
5. How this fits into the larger RAG pipeline (feeds into Tutorial 02: Chunking)

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/documents/upload` | Upload and parse a document |
| GET | `/api/documents` | List all parsed documents |
| GET | `/api/documents/{id}` | Get parsed document by ID |
| DELETE | `/api/documents/{id}` | Delete a document |

## 📋 Prerequisites

- Python 3.11+ and Node.js 18+
- No prior RAG knowledge needed — this is the starting point

## ✏️ Exercises

Try these after completing the tutorial:

1. **Add a new format**: Extend the API to parse `.csv` or `.html` files
2. **Metadata enrichment**: Extract the document's language, reading level, or word frequency
3. **Stress test**: Upload a 500-page PDF and a 1KB text file — how does performance differ?
4. **Error handling**: Create a corrupted PDF and ensure the API returns a useful error, not a crash
5. **Batch upload**: Modify the API to accept a ZIP file with multiple documents inside

## ⚠️ Common Mistakes

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| Extracted text has `\x00` or garbage characters | PDF has embedded fonts or encoding issues | Add a text cleaning step: strip non-printable chars |
| DOCX parser misses text in headers/footers | python-docx reads body paragraphs only by default | Explicitly iterate over headers, footers, and tables |
| Scanned PDF returns empty text | PyPDF2 can't OCR — it only extracts embedded text | Add Tesseract OCR as a fallback for image-based PDFs |
| Large files crash the server | No file size limit on the upload endpoint | Add a max file size check (e.g., 50MB) in the API |

## 📚 Further Reading

- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/) — PDF parsing internals
- [python-docx Documentation](https://python-docx.readthedocs.io/) — DOCX structure and extraction
- [Unstructured.io](https://unstructured.io/) — Production-grade document parsing library
- [Apache Tika](https://tika.apache.org/) — Multi-format parser used in enterprise search

## ➡️ Next Steps

Once you can reliably parse documents into clean text, head to **[Tutorial 02 — Chunking Strategies](https://github.com/kishore2797/rag-02-chunking-strategies)** to learn how to split that text into optimal pieces for embedding and retrieval.

---

<p align="center">
  <sub>Part of <a href="https://github.com/kishore2797/mastering-rag">Mastering RAG — From Zero to Production</a></sub>
</p>

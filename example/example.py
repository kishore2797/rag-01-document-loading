#!/usr/bin/env python3
"""
RAG Tutorial 01 — Document Loading & Parsing
Minimal example: load PDF and plain text, extract text and metadata.
Run: pip install -r requirements.txt && python example.py
"""
import os
from pathlib import Path

# PDF
try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None


def load_pdf(path: str) -> dict:
    """Extract text and metadata from a PDF."""
    if not PdfReader:
        return {"text": "", "metadata": {"error": "pypdf not installed"}, "format": "pdf"}
    reader = PdfReader(path)
    text = "\n".join(p.extract_text() or "" for p in reader.pages)
    meta = reader.metadata or {}
    return {
        "text": text.strip(),
        "metadata": {
            "source": path,
            "pages": len(reader.pages),
            "format": "pdf",
            "title": meta.get("/Title", ""),
        },
        "format": "pdf",
    }


def load_txt(path: str) -> dict:
    """Load plain text with metadata."""
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()
    return {
        "text": text.strip(),
        "metadata": {
            "source": path,
            "format": "txt",
            "size_bytes": os.path.getsize(path),
        },
        "format": "txt",
    }


def load_document(path: str) -> dict:
    """Unified loader: dispatch by extension."""
    p = Path(path)
    if not p.exists():
        return {"text": "", "metadata": {"error": "file not found"}, "format": ""}
    suf = p.suffix.lower()
    if suf == ".pdf":
        return load_pdf(path)
    if suf in (".txt", ".md", ".text"):
        return load_txt(path)
    return {"text": "", "metadata": {"error": f"unsupported format: {suf}"}, "format": ""}


if __name__ == "__main__":
    # Create a sample text file and load it
    sample_txt = Path(__file__).parent / "sample.txt"
    sample_txt.write_text(
        "Hello from RAG Tutorial 01.\n\n"
        "Document loading is the first step: extract clean text from PDFs, DOCX, and plain text.",
        encoding="utf-8",
    )
    out = load_document(str(sample_txt))
    print("Loaded document:")
    print("  format:", out["format"])
    print("  metadata:", out["metadata"])
    print("  text (first 80 chars):", (out["text"] or "")[:80] + "...")
    # If you have a PDF, try: load_document("path/to/file.pdf")
    sample_txt.unlink(missing_ok=True)

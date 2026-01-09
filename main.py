from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pdf2docx import Converter
import uuid
import os

app = FastAPI()

UPLOAD_DIR = "files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/convert")
async def convert_pdf_to_word(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files allowed"}

    pdf_path = f"{UPLOAD_DIR}/{uuid.uuid4()}.pdf"
    docx_path = pdf_path.replace(".pdf", ".docx")

    # Save uploaded PDF
    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    # Convert PDF → DOCX
    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()

    return FileResponse(
        docx_path,
        filename="converted.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

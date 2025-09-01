# 📄 PDF Watermark API
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  [![Made with Flask](https://img.shields.io/badge/Made%20with-Flask-blue.svg)](https://flask.palletsprojects.com/)  [![Powered by PyMuPDF](https://img.shields.io/badge/PDF-PyMuPDF-orange.svg)](https://pymupdf.readthedocs.io/)  [![Deploy on Vercel](https://img.shields.io/badge/Deploy-Vercel-black.svg)](https://vercel.com/)  [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)  


This project is a simple Flask-based API for watermarking PDF files with a **student ID**.
It takes a PDF file and overlays the given student ID text repeatedly across every page, generating a new **watermarked PDF**.

---

## 🚀 Features

* Upload any PDF and add a **student ID watermark** automatically
* Lightweight API built with **Flask**
* Uses **PyMuPDF (fitz)** for PDF manipulation
* Ready to deploy on **Vercel**
* Returns the watermarked PDF directly as a downloadable file

---

## 📂 Project Structure

```
├── main.py          # Flask application with watermark API
├── requirements.txt # Project dependencies
├── vercel.json      # Vercel deployment configuration
├── .gitignore       # Git ignored files (Python defaults)
└── LICENSE          # MIT License
```

---

## ⚙️ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/vasantharan/PDF_Watermark_API.git
cd PDF_Watermark_API
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask server

```bash
python main.py
```

Server will start at:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📌 API Endpoints

### **`GET /`**

* Returns a simple welcome message with API usage instructions.

### **`POST /watermark`**

Watermarks a given PDF with the provided student ID.

**Form Data:**

* `student_id` → (string) ID to watermark on PDF
* `pdf_file` → (file) PDF document to be watermarked

**Example (using curl):**

```bash
curl -X POST http://127.0.0.1:5000/watermark \
  -F "student_id=123456" \
  -F "pdf_file=@sample.pdf" \
  --output watermarked.pdf
```

Response: A **downloadable PDF** (`watermarked.pdf`) with the watermark applied.

---

## 🌐 Deployment on Vercel

This project is pre-configured for **Vercel** using `vercel.json`.

To deploy:

```bash
vercel
```

After successful deployment, your API will be available on your Vercel domain.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
You’re free to use, modify, and distribute it.

---

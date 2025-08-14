from flask import Flask, request, send_file
import fitz  
from io import BytesIO

app = Flask(__name__)

@app.route("/watermark", methods=["POST", "GET"])
def home():
    return "API for watermarking PDFs with student IDs. Use POST /watermark to watermark a PDF."

@app.route("/watermark", methods=["POST"])
def watermark_pdf():
    student_id = request.form.get("student_id")
    if not student_id:
        return "Missing student_id", 400
    pdf_file = request.files.get("pdf_file")
    if not pdf_file:
        return "Missing pdf_file", 400
    pdf_bytes = pdf_file.read()
    pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = student_id
    fontsize = 10
    color = (0.95, 0.95, 0.95)
    rotation = 0
    for page_num in range(pdf_doc.page_count):
        page = pdf_doc[page_num]
        page_rect = page.rect
        x_spacing = 70
        y_spacing = 50

        y = 0
        while y < page_rect.height + y_spacing:
            x = 0
            while x < page_rect.width + x_spacing:
                page.insert_text(
                    (x, y),
                    text,
                    fontsize=fontsize,
                    color=color,
                    rotate=rotation
                )
                x += x_spacing
            y += y_spacing
    output = BytesIO()
    pdf_doc.save(output)
    pdf_doc.close()
    output.seek(0)
    return send_file(
        output,
        mimetype="application/pdf",
        as_attachment=True,
        download_name="watermarked.pdf"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, request, send_file
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Замените "path/to/pdf.pdf" на путь к вашему PDF файлу
PDF_FILE = "path/to/pdf.pdf"

@app.route("/pdf", methods=["POST"])
def send_pdf():
    try:
        # Получите ID чата из запроса
        chat_id = request.form["chat_id"]

        # Отправьте PDF файл в чат
        return send_file(PDF_FILE, mimetype="application/pdf", as_attachment=True,
                         attachment_filename="downloaded_pdf.pdf")

    except KeyError:
        return BadRequest("Missing chat_id parameter")

if __name__ == "__main__":
    app.run(debug=True)
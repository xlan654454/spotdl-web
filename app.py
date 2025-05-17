from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = "downloads"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            os.system(f"spotdl download {url} --output {DOWNLOAD_FOLDER}")
            filename = os.listdir(DOWNLOAD_FOLDER)[0]
            return send_file(os.path.join(DOWNLOAD_FOLDER, filename), as_attachment=True)
    return render_template("index.html")

if __name__ == "__main__":
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)
    app.run(host="0.0.0.0", port=5000)

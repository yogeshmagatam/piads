from flask import Flask, request, send_file, render_template

app = Flask(__name__)

uploaded_files = []

def get_uploaded_files():
    return uploaded_files

@app.route('/')
def index():
    files = get_uploaded_files()
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = file.filename
        try:
            file.save('uploads/' + filename)
            uploaded_files.append(filename)
            return 'File uploaded successfully'
        except Exception as e:
            return f"Upload failed: {str(e)}"
    else:
        return 'No file uploaded'

@app.route('/download/<filename>')
def download_file(filename):
    path = 'uploads/' + filename
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
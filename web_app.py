import os
from flask import Flask, request, send_file, render_template, redirect, url_for, jsonify

app = Flask(__name__)

uploaded_files = []

UPLOAD_FOLDER = 'uploads'

# Ensure the uploads directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True    )

def get_uploaded_files():
    try:
        return os.listdir(UPLOAD_FOLDER)
    except Exception:
        return []

@app.route('/')
def index():
    files = get_uploaded_files()
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file:
        filename = file.filename
        try:
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            # If AJAX, return JSON
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'success': True, 'filename': filename}), 200
            # Else, normal redirect
            return redirect(url_for('index'))
        except Exception as e:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'success': False, 'error': str(e)}), 500
            return f"Upload failed: {str(e)}"
    else:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'success': False, 'error': 'No file uploaded'}), 400
        return 'No file uploaded'

@app.route('/download/<filename>')
def download_file(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
import os
from flask import Flask, request, render_template, redirect, url_for, jsonify, send_from_directory

app = Flask(__name__)

MEDIA_FOLDER = os.path.join(os.path.dirname(__file__), 'pi_files', 'media')
os.makedirs(MEDIA_FOLDER, exist_ok=True)

def get_uploaded_videos():
    try:
        return [f for f in os.listdir(MEDIA_FOLDER) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]
    except Exception:
        return []

@app.route('/')
def index():
    videos = get_uploaded_videos()
    return render_template('index.html', videos=videos)

@app.route('/upload_video', methods=['POST'])
def upload_video():
    file = request.files.get('video')
    if file and file.filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
        filename = file.filename
        try:
            file.save(os.path.join(MEDIA_FOLDER, filename))
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
            return jsonify({'success': False, 'error': 'Invalid or no file uploaded'}), 400
        return 'Invalid or no file uploaded'

@app.route('/media/<filename>')
def serve_video(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
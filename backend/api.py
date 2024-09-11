from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from video_prediction import StartApplication

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploaded_videos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/process_video', methods=['POST'])
def process_video():
    if 'video' not in request.files:
        return jsonify({"error": "No video file provided"}), 400

    video_file = request.files['video']

    if video_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    video_path = os.path.join(UPLOAD_FOLDER, video_file.filename)
    video_file.save(video_path)

    output_video_path = f"output_{video_file.filename}"

    try:
        results = StartApplication(video_path, output_video_path)
        print(results)
        return jsonify({"message": f"{results}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
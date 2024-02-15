from flask import Flask, render_template, request
from ultralytics import YOLO
import os

app = Flask(__name__)

# loading pre-trained model
model = YOLO('wallModel.pt')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded video file
        video = request.files['video']

        if video:
            # Save the video to a temporary location
            video_path = 'static/uploads/input_video.mp4'
            video.save(video_path)

            # Perform crack detection
            results = model(source=video_path, show=True, conf=0.3, save=True)

            # Return the path to the output video
            output_video_path = 'static/uploads/output_video.mp4'
            return render_template('index.html', input_video=video_path, output_video=output_video_path)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
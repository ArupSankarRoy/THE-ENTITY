import os
from entity_main_package.pipeline.training_pipeline import TrainPipeline
from flask import Flask, request, jsonify, render_template,Response, request, redirect, url_for,session
from flask_socketio import SocketIO
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import base64
import cv2
import shutil
import random
import math
from ultralytics import YOLO
from ultralytics.solutions import heatmap
from entity_main_package.logger import logging
from entity_main_package.constant.application import APP_HOST, APP_PORT



app = Flask(__name__)
socketio = SocketIO(app)
#--------------------------------------------------------LOGIN----------------------------------------------------------------------------
app.secret_key = 'xyzsdfg'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'user-system'
app.config['MYSQL_PORT'] = 3308  # Replace with your MySQL port

mysql = MySQL(app)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password,))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            message = 'Logged in successfully!'
            return render_template('user.html', message=message)
        else:
            message = 'Please enter correct email / password!'
    return render_template('login.html', message=message)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        try:
            cursor.execute('INSERT INTO user (`name`, `email`, `password`) VALUES (%s, %s, %s)', (userName, email, password,))
            mysql.connection.commit()
            message = 'You have successfully registered!'
            return redirect(url_for('login'))
        except MySQLdb.Error as e:
            print("MySQL Error during registration:", e)
            mysql.connection.rollback()  # Rollback in case of an error
            message = 'An error occurred during registration.'

    elif request.method == 'POST':
        message = 'Please fill out the form!'

    return render_template('register.html', message=message)

#-------------------------------------------------------TRAIN-----------------------------------------------------------------------------
@app.route("/train")
def trainRoute():
    training = True

    if training:
        obj = TrainPipeline()
        obj.run_pipeline()
        return render_template('train.html')
    return redirect(url_for('train.html'))


#-----------------------------------------------------VIDEO STREAMING---------------------------------------------------------------------
UPLOAD_FOLDER_VIDEO = 'staticVideoStore'
app.config['UPLOAD_FOLDER_VIDEO'] = UPLOAD_FOLDER_VIDEO

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mkv', 'mov'} 

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/user', methods=['GET', 'POST'])
def upload_file_video():
    os.makedirs(UPLOAD_FOLDER_VIDEO, exist_ok=True)
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('user.html', error='No file part')

        file = request.files['file']

        if file.filename == '':
            return render_template('user.html', error='No selected file')

        if file and allowed_file(file.filename):
            
            # Rename the file as 'input_user_video'
            filename = os.path.join(app.config['UPLOAD_FOLDER_VIDEO'], 'input_user_video.' + file.filename.rsplit('.', 1)[1].lower())
            if len(os.listdir('staticVideoStore')) == 0:
               file.save(filename)

            else:
                shutil.rmtree(UPLOAD_FOLDER_VIDEO)
                os.makedirs(UPLOAD_FOLDER_VIDEO, exist_ok=True)
                file.save(filename)

            return render_template('user.html', success='File uploaded successfully')

    return render_template('user.html')


def gen(cap_video, frame_wid=1000, frame_hyt=600, class_list=None, detection_colors=None, model=YOLO('MODELS\detections\weapon_detection_best.pt')):
    try:
        while True:
            ret, frame = cap_video.read()

            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            frame = cv2.resize(frame, (int(frame_wid), int(frame_hyt)))

            detect_params = model.predict(source=[frame], conf=0.4, save=False)

            if len(detect_params[0].numpy()) != 0:
                for i, box in enumerate(detect_params[0].boxes):
                    clsID = box.cls.numpy()[0]
                    conf = box.conf.numpy()[0]
                    bb = box.xyxy.numpy()[0]

                    cv2.rectangle(
                        frame,
                        (int(bb[0]), int(bb[1])),
                        (int(bb[2]), int(bb[3])),
                        detection_colors[int(clsID)],
                        3,
                    )

                    font = cv2.FONT_HERSHEY_COMPLEX
                    cv2.putText(
                        frame,
                        f"{class_list[int(clsID)]} {round(conf * 100, 3)}%",
                        (int(bb[0]), int(bb[1]) - 10),
                        font,
                        1,
                        (255, 255, 255),
                        2,
                    )

            # Encode the frame as JPEG before yielding
            _, encoded_frame = cv2.imencode('.jpg', frame)
            frame_bytes = encoded_frame.tobytes()

            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    except Exception as e:
        print(f"Error in gen function: {e}")
    finally:
        if cap_video:
            cap_video.release()

@app.route('/streaming')
def video_feed_streaming():
    logging.info('Video Streaming running...')
    if len(os.listdir('staticVideoStore')) >= 1:
            
            file_name = os.listdir('staticVideoStore')
            video_path = f'staticVideoStore/{file_name[0]}'
            my_file = open(r"entity_main_package\utils\samples.txt", "r")
            data = my_file.read()
            class_list = data.split("\n")
            my_file.close()
            detection_colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                                for _ in range(len(class_list))]

            cap_video = cv2.VideoCapture(video_path)

            if not cap_video.isOpened():
                print("Cannot open video file:", video_path)
                exit()

            return Response(gen(cap_video=cap_video,class_list= class_list, detection_colors=detection_colors),
                                mimetype='multipart/x-mixed-replace; boundary=frame')

    return render_template('video.html')

#-----------------------------------------------------IMAGE PREDICTION---------------------------------------------------------------------
UPLOAD_FOLDER_IMAGE = 'static'
app.config['UPLOAD_FOLDER_IMAGE'] = UPLOAD_FOLDER_IMAGE

# Default image URL
DEFAULT_IMAGE_URL = "https://th.bing.com/th/id/OIG1.nkMOwh2Z3kRZeydyJMkl?w=270&h=270&c=6&r=0&o=5&dpr=1.3&pid=ImgGn"

@app.route('/predictFromImage', methods=['GET', 'POST'])
def upload_file_image():
    logging.info('Predict from image has start...')
    os.makedirs(UPLOAD_FOLDER_IMAGE, exist_ok=True)
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('image.html', error='No file part', default_image=DEFAULT_IMAGE_URL)

        file = request.files['file']

        if file.filename == '':
            return render_template('image.html', error='No selected file', default_image=DEFAULT_IMAGE_URL)

        if file:
            # Rename the file as 'input_Image'
            filename = os.path.join(app.config['UPLOAD_FOLDER_IMAGE'], 'input_Image.jpg')  # You can adjust the file extension as needed
            file.save(filename)
            
            # Extract the filename from the full path
            displayed_filename = os.path.basename(filename)
            
            return render_template('image.html', success='File uploaded successfully', uploaded_image=filename, displayed_filename=displayed_filename)

    return render_template('image.html', default_image=DEFAULT_IMAGE_URL)


# Instantiate multiple models outside the thread
shared_model_1 = YOLO("MODELS\detections\weapon_detection_best.pt")
shared_model_2 = YOLO("MODELS\segments\weapon_segment_best.pt")

def predict(model, image_path):
        results = model.predict(image_path, save=True, conf=0.2)
        # Process results

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' successfully renamed to '{new_name}'.")
    except FileNotFoundError:
        print(f"Error: File '{old_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def copy_file(source_path, destination_path):
    try:
        shutil.copy(source_path, destination_path)
        print(f"File '{source_path}' successfully copied to '{destination_path}'.")
    except FileNotFoundError:
        print(f"Error: File '{source_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def create_heatmap(input_img_path, model):
    im0 = cv2.imread(input_img_path)  

    # Heatmap Init
    heatmap_obj = heatmap.Heatmap()
    heatmap_obj.set_args(colormap=cv2.COLORMAP_JET,
                        imw=im0.shape[0],
                        imh=im0.shape[1],
                        view_img=False)

    # Run YOLO tracking
    results = model.track(im0, persist=True)

    # Generate and save heatmap image
    output_image_path = "static/output_heatmap_img.jpg" 
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)  
    im0 = heatmap_obj.generate_heatmap(im0, tracks=results)
    cv2.imwrite(output_image_path, im0)

@app.route('/predict_Image')
def main_predict_function():
    try:
        # Get absolute paths
        base_dir = os.path.dirname(os.path.abspath(__file__))
        input_image_path = os.path.join(base_dir, 'static', 'input_Image.jpg')

        predict(shared_model_1 , input_image_path)
        predict(shared_model_2 , input_image_path)

        # Rename and copy detect image
        old_file_name_detect = os.path.join(base_dir, 'runs', 'detect', 'predict', 'input_Image.jpg')
        new_file_name_detect = os.path.join(base_dir, 'runs', 'detect', 'predict', 'output_detect_img.jpg')
        rename_file(old_file_name_detect, new_file_name_detect)
        copy_file(new_file_name_detect, os.path.join(base_dir, 'static'))

        # Rename and copy segment image
        old_file_name_segment = os.path.join(base_dir, 'runs', 'segment', 'predict', 'input_Image.jpg')
        new_file_name_segment = os.path.join(base_dir, 'runs', 'segment', 'predict', 'output_segment_img.jpg')
        rename_file(old_file_name_segment, new_file_name_segment)
        copy_file(new_file_name_segment, os.path.join(base_dir, 'static'))

        # Create heatmap using shared_model_1
        create_heatmap(input_img_path=input_image_path, model=shared_model_1)

        # Delete the 'runs' folder
        shutil.rmtree(os.path.join(base_dir, 'runs'))

        app.logger.info('Prediction successful')
        return jsonify({'message': 'Prediction complete'})
    except Exception as e:
        app.logger.error(f'Prediction failed: {str(e)}')
        return jsonify({'error': str(e)})
    
#-----------------------------------------------------LIVE-------------------------------------------------------------------------
    
def detect_objects(frame):

    model = YOLO("MODELS\detections\weapon_detection_best.pt")
    my_file = open(r"entity_main_package\utils\samples.txt", "r")
    data = my_file.read()
    classNames = data.split("\n")
    results = model(frame, stream=True, conf=0.10)

    for r in results:
        boxes = r.boxes

        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

            confidence = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])

            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(frame, classNames[cls], org, font, fontScale, color, thickness)

    return frame

def generate_frames():

    # OpenCV video capture
    cap_live = cv2.VideoCapture(0)
    cap_live.set(3, 640)
    cap_live.set(4, 480)

    while True:
        success, frame = cap_live.read()
        if not success:
            break
        else:
            frame = detect_objects(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/live')
def index():
    logging.info('live detection from webcam starts...')
    return render_template('live.html')

@app.route('/video_feed_live')
def video_feed_live():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)

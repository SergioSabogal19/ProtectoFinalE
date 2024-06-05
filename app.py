from flask import Flask, render_template, Response, request, jsonify
import cv2
import numpy as np
import base64

app = Flask(__name__)

kernel_detection_edges = np.array([[1, 0, -1],
                                   [2, 0, -2],
                                   [1, 0, -1]])

kernel_smoothing = np.array([[1/9, 1/9, 1/9],
                             [1/9, 1/9, 1/9],
                             [1/9, 1/9, 1/9]])

kernel_edge_enhancement = np.array([[0, 1, 0],
                                    [1, -4, 1],
                                    [0, 1, 0]])

def gen_frames():
    camera = cv2.VideoCapture(1)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/motor')
def motor():
    return render_template('motor.html')

@app.route('/run_function', methods=['POST'])
def run_function():
    opcion_seleccionada = request.form.get('opciones')
    if opcion_seleccionada:
        resultado = my_python_function(opcion_seleccionada)
    else:
        return 'No se ha seleccionado ninguna opción.'

def my_python_function(opcion):
    camera = cv2.VideoCapture(1)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            if opcion == 'opcion1':
                frame = cv2.filter2D(frame, -1, kernel_detection_edges)
            elif opcion == 'opcion2':
                frame = cv2.filter2D(frame, -1, kernel_smoothing)
            elif opcion == 'opcion3':
                frame = cv2.filter2D(frame, -1, kernel_edge_enhancement)
            else:
                return "Opción no válida"
            
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


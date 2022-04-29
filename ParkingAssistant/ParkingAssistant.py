from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__)
sliderValue = 0
fps = 30
frame_width = 640
frame_height = 480

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
cap.set(cv2.CAP_PROP_FPS, fps)


def correctLines():
    while True:
        value = 0
        ret, frame = cap.read()
        if(sliderValue == 1):
            value = 425
            img = cv2.line(frame, (213, 250), (427, 250), (0, 255, 0), 3)
            img = cv2.line(frame, (164, 290), (476, 290), (0, 255, 0), 4)
            img = cv2.line(frame, (97, 350), (542, 350), (45, 255, 255), 3)
            img = cv2.line(frame, (95, 353), (545, 353), (45, 255, 255), 3)
            img = cv2.line(frame, (25, 410),  (615, 410), (0, 0, 255), 4)
            img = cv2.line(frame, (22, 413),  (618, 413), (0, 0, 255), 4)
            img = cv2.line(frame, (19, 416),  (621, 416), (0, 0, 255), 4)
        elif(sliderValue == 2):
            value = 405
            img = cv2.line(frame, (213, 250), (427, 250), (0, 255, 0), 3)
            img = cv2.line(frame, (164, 290), (476, 290), (0, 255, 0), 4)
            img = cv2.line(frame, (97, 337), (542, 337), (45, 255, 255), 3)
            img = cv2.line(frame, (95, 340), (545, 340), (45, 255, 255), 3)
            img = cv2.line(frame, (27, 387),  (614, 387), (0, 0, 255), 4)
            img = cv2.line(frame, (24, 390),  (617, 390), (0, 0, 255), 4)
            img = cv2.line(frame, (21, 393),  (620, 393), (0, 0, 255), 4)
        elif(sliderValue == 3):
            value = 385
            img = cv2.line(frame, (213, 250), (427, 250), (0, 255, 0), 3)
            img = cv2.line(frame, (164, 283), (476, 283), (0, 255, 0), 4)
            img = cv2.line(frame, (97, 317), (542, 317), (45, 255, 255), 3)
            img = cv2.line(frame, (95, 320), (545, 320), (45, 255, 255), 3)
            img = cv2.line(frame, (27, 369),  (614, 369), (0, 0, 255), 4)
            img = cv2.line(frame, (24, 372),  (617, 372), (0, 0, 255), 4)
            img = cv2.line(frame, (21, 375),  (620, 375), (0, 0, 255), 4)
        pixels = [value, value-4, value-8, value-12, value-16, value-20]
        for i in pixels:
            img = cv2.line(frame, (640, i), (430, 250), (255, 0, 0), 5)
        pixels1 = [value, value-4, value-8, value-12, value-16, value-20]
        for i in pixels1:
            img = cv2.line(frame, (0, i), (210, 250), (255, 0, 0), 5)

        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def videoWithDefaultLines():
    while True:
        ret, frame = cap.read()
   
        img = cv2.line(frame, (213, 250), (427, 250), (0, 255, 0), 3)
        img = cv2.line(frame, (170, 290), (473, 290), (0, 255, 0), 4)
        img = cv2.line(frame, (108, 350), (530, 350), (45, 255, 255), 3)
        img = cv2.line(frame, (105, 353), (533, 353), (45, 255, 255), 3)
        img = cv2.line(frame, (33, 420),  (606, 420), (0, 0, 255), 4)
        img = cv2.line(frame, (30, 423),  (609, 423), (0, 0, 255), 4)
        img = cv2.line(frame, (28, 426),  (612, 426), (0, 0, 255), 4)
        pixels = [445, 441, 437, 433, 429, 425]
        for i in pixels:
            img = cv2.line(frame, (0, i), (210, 250), (255, 0, 0), 5)
        pixels1 = [445, 441, 437, 433, 429, 425]
        for i in pixels1:
            img = cv2.line(frame, (640, i), (430, 250), (255, 0, 0), 5)
        ret, buffer = cv2.imencode('.jpg', img)

        img = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')


def videoWithNoLines():
    while True:
        ret, frame = cap.read()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/defaultLines')
def defaultLines():
    return Response(videoWithDefaultLines(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/videoStreamWithNoLines')
def videoStreamWithNoLines():
    return Response(videoWithNoLines(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/noLines')
def noLines():
    return render_template('noLines.html')


@app.route('/videoStreamCorrectedLines')
def videoStreamCorrectedLines():
    return Response(correctLines(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/correctedLines", methods=["POST"])
def correctedLines():
    global sliderValue
    sliderValue = int(request.form["sliderValue"])
    return render_template('cLines.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

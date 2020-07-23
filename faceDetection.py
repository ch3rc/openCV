import cv2


def createSquare(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)

    face = faces.detectMultiScale(frame_gray)

    for (x, y, w, h) in face:
	frame = cv2. rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)


# get path of haar cascade pre-trained model
# side note add cv2.data.haarcascades to get
# full file path or you will get an error
path = "haarcascade_frontalface_default.xml"
faces = cvw.CascadeClassifier(cv2.data.haarcascades + path)

#set video capture to zero'th id
vid = cv2.VideoCapture(0)
if not vid.isOpened:
    print('Error opening video capture')
    exit(0)

while True:
    # capture video frame by frame
    ret, frame = vid.read()

    if frame is None:
	printf('No video captured')
	break

    createSquare(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
	break

vid.release()

cv2.destroyAllWindows()

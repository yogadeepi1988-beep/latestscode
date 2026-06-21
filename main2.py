import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    # ret (short for "return") is a boolean value (True or False) that indicates whether the frame was read successfully or not.
    ret, frame = cap.read()

    # If frame is read correctly, ret will be True
    if not ret:
        print("Error: Failed to capture image")
        break

    #gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect faceles in grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

    #Draw a rectangle around imade
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)

    #Display no of faces
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f'people count: {len(faces)}', (10,30), font, 1, (123,125,123),2,cv2.LINE_AA)

    #Display the frame with face detection and people count
    cv2.imshow('Face Tracking and counting',frame)

    #Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Relase the webcam and close the window
cap.release()
cv2.destroyAllWindows()
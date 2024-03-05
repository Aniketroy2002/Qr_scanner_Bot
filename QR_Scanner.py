import cv2      #For accessing camera.
import time
import webbrowser as wb     #For accessing online links.
detect=cv2.QRCodeDetector()
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    try:
            data,var,_=detect.detectAndDecode(frame)
            if data:
                url=data
                break
    except Exception as e:          #Exception handeling.
        print("QR code not found")
    cv2.imshow("camera",frame)
    if cv2.waitKey(1) & 0xFF==ord('a'): #For close the camera.
        break
cap.release()
cv2.destroyAllWindows()
time.sleep(2)
wb.open(url)
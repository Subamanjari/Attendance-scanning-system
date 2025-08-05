
import cv2
from pyzbar.pyzbar import decode
import time


cap = cv2.VideoCapture(0)
  
if not cap.isOpened():
    print("❌ Error: Cannot open webcam")
    exit()

while True:
    ret, frame = cap.read()

    if not ret or frame is None:
        print("⚠️ Warning: Couldn't read from camera.")
        continue

    
    codes = decode(frame)
    for code in codes:
        data = code.data.decode('utf-8')
        print("✅ present:", data)

       
        pts = code.polygon
        if pts:
            pts = [(pt.x, pt.y) for pt in pts]
            for i in range(len(pts)):
                cv2.line(frame, pts[i], pts[(i + 1) % len(pts)], (0, 255, 0), 3)

        cv2.putText(frame, data, (code.rect.left, code.rect.top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        time.sleep(2)
        cap.release()
        cv2.destroyAllWindows()
        exit()


    cv2.imshow("QR Scanner - Press Q to quit", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
import cv2
from pyzbar.pyzbar import decode
import time


cap = cv2.VideoCapture(0)
  
if not cap.isOpened():
    print("❌ Error: Cannot open webcam")
    exit()

while True:
    ret, frame = cap.read()

    if not ret or frame is None:
        print("⚠️ Warning: Couldn't read from camera.")
        continue

    
    codes = decode(frame)
    for code in codes:
        data = code.data.decode('utf-8')
        print("✅ present:", data)

       
        pts = code.polygon
        if pts:
            pts = [(pt.x, pt.y) for pt in pts]
            for i in range(len(pts)):
                cv2.line(frame, pts[i], pts[(i + 1) % len(pts)], (0, 255, 0), 3)

        cv2.putText(frame, data, (code.rect.left, code.rect.top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        time.sleep(2)
        cap.release()
        cv2.destroyAllWindows()
        exit()


    cv2.imshow("QR Scanner - Press Q to quit", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

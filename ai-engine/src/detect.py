from ultralytics import YOLO
import cv2
import requests
import time

# 🔥 Your C# API endpoint — this is where alerts will be sent
C_SHARP_API = "http://localhost:5000/api/alert"

def send_alert_to_csharp(object_detected):
    """Send alert to a C# API."""
    try:
        print(f"Sending alert: {object_detected}")
        payload = {"alert": f"{object_detected} detected"}
        requests.post(C_SHARP_API, json=payload, timeout=3)
    except Exception as e:
        print(f"Failed to send alert to C#: {e}")


def start_detection():
    print("Starting SafeVision AI detection...")

    # Load your custom gun-detection model
    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot access the webcam.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Frame read error, skipping...")
                continue

            results = model(frame)

            # Loop through detected objects
            for r in results:
                for box in r.boxes:
                    cls = int(box.cls[0])
                    class_name = model.names[cls]  # e.g., "person", "gun", "knife"

                    # 👇 CHANGE THIS based on your custom model class labels
                    if class_name.lower() in ["gun", "pistol", "rifle"]:
                        print("⚠️ WEAPON DETECTED!")
                        send_alert_to_csharp(class_name)

            annotated = results[0].plot()
            cv2.imshow("SafeVision AI - Detection", annotated)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:
                print("Exiting...")
                break

    except KeyboardInterrupt:
        print("Stopped manually.")
    except Exception as e:
        print(f"Runtime Error: {e}")

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("System closed.")


if __name__ == "__main__":
    start_detection()

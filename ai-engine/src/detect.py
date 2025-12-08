from ultralytics import YOLO
import cv2

def start_detection():
    print("Starting SafeVision AI detection...")
    model = YOLO("yolov8n.pt")
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot access the webcam.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Warning: Frame not read properly, skipping...")
                continue

            results = model(frame)
            annotated = results[0].plot()

            cv2.imshow("SafeVision AI - Detection", annotated)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:  # 'q' or Esc to quit
                print("Detection stopped by user.")
                break
    except KeyboardInterrupt:
        print("Detection interrupted via Ctrl+C.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("Resources released. Exiting.")

if __name__ == "__main__":
    start_detection()

import cv2
from ultralytics import YOLO
# Charger le modèle YOLO (léger et rapide)
model = YOLO("yolov8n.pt")

# Ouvrir la webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Détection
    results = model(frame)

    for r in results:
        for box in r.boxes:
            # Coordonnées du carré
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Classe et probabilité
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            label = f"{model.names[cls_id]} {conf*100:.0f}%"

            # Dessiner le carré
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Afficher le texte
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Reconnaissance IA", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC pour quitter
        break

cap.release()
cv2.destroyAllWindows()

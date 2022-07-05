import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd ="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
config = 'digits'
image = cv2.imread("images\ocr_sample.jpg")
RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(RGB_img))
results = pytesseract.image_to_boxes(RGB_img)
ih, iw, ic = image.shape
for box in results.splitlines():
    box = box.split(' ')
    print(box)

    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(image, (x, ih-y), (w, ih-h), (0, 255, 0), 2)
    cv2.putText(image, box[0], (x, ih-h), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
cv2.imshow("input", image)
cv2.waitKey(0)
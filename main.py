import pytesseract
import cv2
caminho = "C:\Program Files\Tesseract-OCR"
imagem = cv2.imread(r"C:\Users\emanu\OneDrive\Documentos\Vscode\crawlers\criminal\documento\indentidade.jpeg")
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagem)
print(texto)
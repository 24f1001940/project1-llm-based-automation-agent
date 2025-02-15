import pytesseract

# Manually set the path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print(f"Tesseract Path: {pytesseract.pytesseract.tesseract_cmd}")

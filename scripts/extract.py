# scripts/extract_text.py
import pytesseract
from PIL import Image

# If on Windows, set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path, lang="ara"):
    """
    Extract text from an image using Tesseract OCR.
    
    Args:
        image_path (str): Path to the image file.
        lang (str): Language code for Tesseract OCR (default is Arabic: 'ara').
    
    Returns:
        str: Extracted text.
    """
    # Open the image
    image = Image.open(image_path)
    
    # Extract text
    text = pytesseract.image_to_string(image, lang=lang)
    return text

if __name__ == "__main__":
    # Example input
    image_path = "../output/trimmed_page1.png"
    extracted_text = extract_text(image_path, lang="ara")
    
    # Save the extracted text
    with open("../output/extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(extracted_text)
    
    print("Extracted text saved to: ../output/extracted_text.txt")

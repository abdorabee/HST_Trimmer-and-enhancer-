# scripts/trim_pdf.py
import fitz  # PyMuPDF

def trim_pdf(input_pdf, page_number, output_image, bbox):
    """
    Trim a part of a PDF page based on the bounding box (bbox).
    
    Args:
        input_pdf (str): Path to the input PDF file.
        page_number (int): Page number to process (0-indexed).
        output_image (str): Path to save the trimmed output as an image.
        bbox (tuple): Bounding box in the format (x0, y0, x1, y1).
        I am not sure about the format 
    """
    # Open the PDF file
    pdf_document = fitz.open(input_pdf)
    
    # Select the page
    page = pdf_document[page_number]
    
    # Clip the page to the bounding box
    clip = page.get_pixmap(clip=bbox)  # Clip and render as an image
    
    # Save the clipped image
    clip.save(output_image)
    print(f"Trimmed part saved to: {output_image}")

if __name__ == "__main__":
    # Example input
    input_pdf = "../input/document.pdf"
    page_number = 0  # First page
    output_image = "../output/trimmed_page1.png"
    bbox = (100, 100, 300, 300)  # Example bounding box (x0, y0, x1, y1)
    
    trim_pdf(input_pdf, page_number, output_image, bbox)

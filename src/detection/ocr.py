from pytesseract import image_to_string

def extract_text(image):
    """
    Extracts text from the given image using Optical Character Recognition (OCR).
    
    Parameters:
        image: The input image from which to extract text.
        
    Returns:
        str: The recognized text from the image.
    """
    # Convert the image to text using pytesseract
    text = image_to_string(image)
    return text.strip()
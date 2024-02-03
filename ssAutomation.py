import os
import cv2
import pytesseract
from PIL import Image
from collections import Counter
import re

def analyze_image(image_path):
    # Use OCR to extract text from the image
    text = pytesseract.image_to_string(Image.open(image_path))
    
    # Tokenize the text into words, filtering out punctuation and making all words lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    # Select the first 4 words
    first_four_words = words[:4]
    
    # Join the first 4 words with underscores to create a filename-friendly string
    keywords = '_'.join(first_four_words)
    
    return keywords

def rename_image(original_path, new_name):
    os.rename(original_path, new_name)

def process_screenshots(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        analysis_result = analyze_image(file_path)
        # Ensure the analysis_result is filename-safe
        analysis_result = analysis_result.replace("/", "_").replace("\\", "_").replace(" ", "_")
        # Generating a unique name to avoid overwriting files with the same analysis_result
        base, extension = os.path.splitext(filename)
        new_name = os.path.join(folder_path, f"{analysis_result}_{base}{extension}")
        rename_image(file_path, new_name)

# Path to the folder where screenshots are saved
screenshot_folder = "your/path"

process_screenshots(screenshot_folder)

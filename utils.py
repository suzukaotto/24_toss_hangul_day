import os
from PIL import Image
import pytesseract
import pyautogui

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_screen_region(_loca1: tuple, _loca2, save_path='captured_region.png'):
    screenshot = pyautogui.screenshot()
    cropped_image = screenshot.crop((_loca1[0], _loca1[1], _loca2[0], _loca2[1]))
    cropped_image.save(save_path)
    
def extract_text_from_image(image_path, lang='kor'):
    img = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(img, lang=lang)
    return extracted_text

def split_image(image_path, n, output_dir):
    img = Image.open(image_path)
    img_width, img_height = img.size

    piece_width = img_width // n
    piece_height = img_height // n

    base_name, ext = os.path.splitext(os.path.basename(image_path))

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for file in os.listdir(output_dir):
        os.remove(os.path.join(output_dir, file))

    for i in range(n):
        for j in range(n):
            left = j * piece_width
            top = i * piece_height
            right = (j + 1) * piece_width
            bottom = (i + 1) * piece_height

            piece = img.crop((left, top, right, bottom))

            piece_number = i * n + j + 1
            piece_path = os.path.join(output_dir, f"y{j+1}_x{i+1}{ext}")
            
            piece.save(piece_path)
            
def find_unique_item(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    
    for item, count in counts.items():
        if count == 1:
            return item
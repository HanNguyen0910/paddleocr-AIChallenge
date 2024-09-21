import os
import csv
from paddleocr import PaddleOCR

# Initialize the OCR model
ocr = PaddleOCR(use_angle_cls=True, lang='vi')  # Initialize the OCR model

# Define the root directory where images are stored
input_folder = '../dataset/keyframes/'
output_folder = 'transcriptions'

def ensure_dir(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)

# Function to process the OCR for each image and save results to CSV
def process_image(image_path, output_csv_path):
    # Apply OCR
    result = ocr.ocr(image_path, cls=True)
    
    # Handle case where OCR result is None or empty
    if result is None or len(result) == 0:
        print(f"No OCR results for: {image_path}, skipping.")
        return
    
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_csv_path)
    ensure_dir(output_dir)

    # Save results to CSV
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['text', 'confidence'])  # Header row
        for idx in range(len(result)):
            res = result[idx]
            if res:  # Check if res is not empty or None
                for line in res:
                    text = line[1][0]  # Detected text
                    score = line[1][1]  # Confidence score
                    writer.writerow([text, score])  # Write each OCR result row
    print(f"OCR results saved for: {image_path}")

# Traverse the input folder and process each JPEG file
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.jpeg'):
            # Full path to the input image
            image_path = os.path.join(root, file)

            # Construct the output CSV path (mirroring the input path in the "transcriptions" folder)
            relative_path = os.path.relpath(image_path, input_folder)  # Get relative path from input folder
            output_csv_path = os.path.join(output_folder, f'{relative_path}.csv')

            # Skip the file if the CSV file already exists
            if os.path.exists(output_csv_path):
                print(f"Skipping {image_path}, CSV already exists.")
                continue

            # Process the image and save results to CSV
            process_image(image_path, output_csv_path)

print("OCR processing complete for all files!")

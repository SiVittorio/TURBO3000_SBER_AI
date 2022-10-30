import easyocr
import csv
import os
import json

def text_recognition(path_to_dir, output_file_name="output.csv"):
    reader = easyocr.Reader(["en", "ru"], verbose=False)

    output = open(output_file_name, "w", newline="", encoding="utf-8")
    writer = csv.DictWriter(output, fieldnames=["image_path", "output"])
    writer.writeheader()

    for image_path in os.listdir(path_to_dir):
        print(f"Processing {image_path}...")

        info = reader.readtext(image_path)
        label = reader.readtext(image_path, detail=0)

        all_texts = []

        for text in info:
            coord = []
            for c in text[0]:
                coord.append(list(map(int, c)))

            all_texts.append({"shape": "rectangle", "coordinates": coord, "label": text[1]})

        writer.writerow({'image_path': image_path, 'output': json.dumps(all_texts)})

text_recognition('.')

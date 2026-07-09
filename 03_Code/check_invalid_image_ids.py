# ============================================================
# VisionAI Logistics AI Quality Assessment
# Script: check_invalid_image_ids.py
# Purpose: Check for annotations that reference invalid images
# ============================================================

import json

# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------

file_path = "02_Data/Original_Annotations/instances_val2017.json"

with open(file_path, "r") as file:
    coco_data = json.load(file)

# ------------------------------------------------------------
# Get all valid image IDs
# ------------------------------------------------------------

valid_image_ids = set()

for image in coco_data["images"]:
    valid_image_ids.add(image["id"])

# ------------------------------------------------------------
# Check annotations
# ------------------------------------------------------------

invalid_image_ids = []

for annotation in coco_data["annotations"]:

    if annotation["image_id"] not in valid_image_ids:
        invalid_image_ids.append(annotation)

# ------------------------------------------------------------
# Results
# ------------------------------------------------------------

print("=" * 50)
print("Invalid Image ID Check")
print("=" * 50)

print(f"Invalid Image References: {len(invalid_image_ids)}")

print("=" * 50)
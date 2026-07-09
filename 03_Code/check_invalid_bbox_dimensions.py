# ============================================================
# VisionAI Logistics AI Quality Assessment
# Script: check_invalid_bbox_dimensions.py
# Purpose: Check for bounding boxes with invalid dimensions
# ============================================================

import json

# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------

file_path = "02_Data/Original_Annotations/instances_val2017.json"

with open(file_path, "r") as file:
    coco_data = json.load(file)

# ------------------------------------------------------------
# Check Bounding Boxes
# ------------------------------------------------------------

invalid_bboxes = []

for annotation in coco_data["annotations"]:

    bbox = annotation["bbox"]

    width = bbox[2]
    height = bbox[3]

    if width <= 0 or height <= 0:
        invalid_bboxes.append(annotation)

# ------------------------------------------------------------
# Results
# ------------------------------------------------------------

print("=" * 50)
print("Invalid Bounding Box Dimension Check")
print("=" * 50)

print(f"Invalid Bounding Boxes: {len(invalid_bboxes)}")

if invalid_bboxes:

    print("\nAffected Annotation IDs:")

    for annotation in invalid_bboxes:
        print(annotation["id"])

print("=" * 50)
# ============================================================
# VisionAI Logistics AI Quality Assessment
# Script: check_bbox_boundaries.py
# Purpose: Check for bounding boxes outside image boundaries
# ============================================================

import json

# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------

file_path = "02_Data/Original_Annotations/instances_val2017.json"

with open(file_path, "r") as file:
    coco_data = json.load(file)

# ------------------------------------------------------------
# Build Image Lookup
# ------------------------------------------------------------

image_lookup = {}

for image in coco_data["images"]:
    image_lookup[image["id"]] = (image["width"], image["height"])

# ------------------------------------------------------------
# Check Bounding Boxes
# ------------------------------------------------------------

invalid_bboxes = []

for annotation in coco_data["annotations"]:

    image_id = annotation["image_id"]
    image_width, image_height = image_lookup[image_id]

    x, y, width, height = annotation["bbox"]

    if (
        x < 0
        or y < 0
        or x + width > image_width
        or y + height > image_height
    ):
        invalid_bboxes.append(annotation)

# ------------------------------------------------------------
# Results
# ------------------------------------------------------------

print("=" * 50)
print("Bounding Box Boundary Check")
print("=" * 50)

print(f"Bounding Boxes Outside Image: {len(invalid_bboxes)}")

if invalid_bboxes:

    print("\nAffected Annotation IDs:")

    for annotation in invalid_bboxes:
        print(annotation["id"])

print("=" * 50)
# ============================================================
# VisionAI Logistics AI Quality Assessment
# Script: check_images_without_annotations.py
# Purpose: Find images that have no annotations
# ============================================================

import json

# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------

file_path = "02_Data/Original_Annotations/instances_val2017.json"

with open(file_path, "r") as file:
    coco_data = json.load(file)

# ------------------------------------------------------------
# Get all image IDs
# ------------------------------------------------------------

all_images = set()

for image in coco_data["images"]:
    all_images.add(image["id"])

# ------------------------------------------------------------
# Get annotated image IDs
# ------------------------------------------------------------

annotated_images = set()

for annotation in coco_data["annotations"]:
    annotated_images.add(annotation["image_id"])

# ------------------------------------------------------------
# Find images without annotations
# ------------------------------------------------------------

images_without_annotations = all_images - annotated_images

# ------------------------------------------------------------
# Display Results
# ------------------------------------------------------------
print("=" * 50)
print("Images Without Annotations")
print("=" * 50)

print(f"Total Images: {len(all_images)}")
print(f"Annotated Images: {len(annotated_images)}")
print(f"Images Without Annotations: {len(images_without_annotations)}")

if images_without_annotations:

    print("\nImage IDs:")

    for image_id in sorted(images_without_annotations):
        print(image_id)

print("=" * 50)

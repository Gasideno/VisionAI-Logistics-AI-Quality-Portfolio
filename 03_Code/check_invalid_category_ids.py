# ============================================================
# VisionAI Logistics AI Quality Assessment
# Script: check_invalid_category_ids.py
# Purpose: Check for annotations with invalid category IDs
# ============================================================

import json

# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------

file_path = "02_Data/Original_Annotations/instances_val2017.json"

with open(file_path, "r") as file:
    coco_data = json.load(file)

# ------------------------------------------------------------
# Get all valid category IDs
# ------------------------------------------------------------

valid_category_ids = set()

for category in coco_data["categories"]:
    valid_category_ids.add(category["id"])

# ------------------------------------------------------------
# Check annotations
# ------------------------------------------------------------

invalid_categories = []

for annotation in coco_data["annotations"]:

    if annotation["category_id"] not in valid_category_ids:
        invalid_categories.append(annotation)

# ------------------------------------------------------------
# Results
# ------------------------------------------------------------

print("=" * 50)
print("Invalid Category ID Check")
print("=" * 50)

print(f"Invalid Category References: {len(invalid_categories)}")

if invalid_categories:

    print("\nAffected Annotation IDs:")

    for annotation in invalid_categories:
        print(annotation["id"])

print("=" * 50)
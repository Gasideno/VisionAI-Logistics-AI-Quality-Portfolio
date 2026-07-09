# ============================================================
# VisionAI Logistics AI Quality Portfolio
# Script: 01_dataset_inventory.py
# Purpose: Load the COCO dataset and display basic statistics.
# ============================================================

import json

# Location of the COCO annotation file
file_path = "02_Data/Original_Annotations/instances_val2017.json"

# Load the JSON dataset
with open(file_path, "r") as file:
    coco_data = json.load(file)

# ------------------------------------------------------------
# Dataset Statistics
# ------------------------------------------------------------

total_images = len(coco_data["images"])
total_categories = len(coco_data["categories"])
total_annotations = len(coco_data["annotations"])

average_annotations = total_annotations / total_images

# ------------------------------------------------------------
# Display Results
# ------------------------------------------------------------

print("=" * 50)
print("VisionAI Logistics")
print("Dataset Inventory Report")
print("=" * 50)

print(f"Total Images: {total_images}")
print(f"Total Categories: {total_categories}")
print(f"Total Annotations: {total_annotations}")
print(f"Average Annotations per Image: {average_annotations:.2f}")

print("=" * 50)
print("Dataset inventory completed successfully.")
print("=" * 50)




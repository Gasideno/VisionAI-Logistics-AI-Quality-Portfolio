# VisionAI Logistics AI Quality Assessment

## Project Overview

This project demonstrates how to perform a structured quality assessment of an AI object detection dataset using Python.

The project uses the COCO 2017 Validation Dataset and performs a series of automated validation checks to identify common dataset quality issues before model training.

---

## Business Problem

Poor-quality datasets lead to poor-performing AI models.

Before training an object detection model, it is important to verify that:

- Images are correctly referenced
- Categories are valid
- Bounding boxes are valid
- Images contain annotations
- Dataset statistics are understood

This project automates those checks and presents the findings in an Excel audit report.

---

## Project Objectives

- Analyse the COCO dataset
- Validate dataset integrity
- Identify common annotation issues
- Generate an Executive Audit Report
- Demonstrate practical AI Data Quality techniques

---

## Tools Used

- Python
- VS Code
- Git
- GitHub
- openpyxl
- JSON

---

## Project Structure

```text
01_Documentation/
02_Data/
03_Code/
04_Reports/
05_Dashboards/
```

---

## Validation Checks

- Dataset Inventory
- Images Without Annotations
- Invalid Image References
- Invalid Category References
- Invalid Bounding Box Dimensions
- Bounding Boxes Outside Image Boundaries

---

## Deliverables

- Executive Audit Report (Excel)
- Validation Scripts
- Development Log
- Documentation

---

## Future Improvements

Project 2 will extend this work by performing image-level quality assessment using computer vision techniques, including:

- Bounding box tightness
- Blur detection
- Image brightness analysis
- Duplicate image detection
- Annotation quality assessment

---

## Author

Kenneth Joachim

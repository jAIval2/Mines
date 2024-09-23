### Project Report

#### **Description**
This project aims to identify mines in a 5x5 matrix of images using pixel comparison. The system analyzes tiles in each image, compares them with reference mine images, and records the coordinates of detected mines. The output is saved in a CSV file with mine coordinates grouped by the image name.

#### **Key Features**
- Detects mines in 5x5 image matrices using pixel analysis.
- Compares tiles with multiple reference images for better accuracy.
- Outputs identified mine coordinates to a CSV file, grouped by image.
- Provides visual plots of the mine positions.

#### **Technologies Used**
- **Python:** Core logic.
- **Pillow (PIL):** Image manipulation.
- **NumPy:** Numerical operations.
- **Pandas:** CSV management.
- **Matplotlib:** Plotting results.

#### **Usage**
- Load multiple images and reference mine images.
- Detect and record mine positions based on pixel correlation.
- Results are saved in a CSV file and visualized in a plot.

Next Steps: Identify an algorithm to process the data about the mines and predict the upcoming location of the mines on providing a few dummy outcomes at first.

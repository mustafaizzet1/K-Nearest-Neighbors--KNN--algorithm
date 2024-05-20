### README

## Diabetes Prediction Application

### Overview

This project is a Python-based application that uses the K-Nearest Neighbors (KNN) algorithm to predict the likelihood of diabetes based on input data. The application includes a graphical user interface (GUI) built with Tkinter, allowing users to input relevant health metrics and receive a prediction about their diabetes status.

### Files

- **diabetes.csv**: The CSV file containing the dataset used for predictions.
- **main.py**: The main Python script containing the logic for data preprocessing, KNN implementation, and the Tkinter GUI.

### Setup Instructions

1. **Install Dependencies**:
   Ensure you have Python installed on your system. Additionally, install Tkinter (if not already installed) and other required libraries using pip:

   ```sh
   pip install tkinter
   ```

2. **CSV File**:
   Make sure `diabetes.csv` is in the same directory as `main.py`. This file should contain the dataset with health metrics and corresponding diabetes outcomes.

### How to Run

1. **Execute the Script**:
   Run the Python script using the following command:

   ```sh
   python main.py
   ```

2. **Using the GUI**:
   - The GUI window will open with entry fields for eight different health metrics.
   - Enter appropriate values for each metric and click the "Get Inputs and Display Result" button.
   - The application will process the inputs, use the KNN algorithm to predict the likelihood of diabetes, and display the result as a percentage.

### Code Explanation

#### Data Handling

- The script reads data from `diabetes.csv` and extracts the first eight columns as feature data (`data`) and the ninth column as the outcome (`outcome`).
- The maximum values for each column are computed to help in the validation and normalization processes.

#### Preprocessing

- **Validation**:
  The `validation` function ensures that the user inputs are within the range of the data in the dataset and can be converted to floating-point numbers.
  
- **Standardization**:
  The `preprocessing` function standardizes the input data using the min-max normalization method, making it suitable for the KNN algorithm.

#### KNN Algorithm

- **Euclidean Distance**:
  The `euclidean_distance` function calculates the distance between two data points in a multidimensional space.
  
- **KNN Implementation**:
  The `knn` function finds the k-nearest neighbors (in this case, 5) and predicts the outcome based on the majority vote.

#### GUI Implementation

- **Input Fields**:
  The GUI has entry fields for each health metric, created dynamically based on the `variables` list.
  
- **Result Display**:
  The result of the KNN prediction is displayed as percentages indicating the likelihood of having diabetes or not.

### Functions

- **`standardization_calculation(list1, max_value, min_value)`**:
  Standardizes the data using min-max normalization.
  
- **`preprocessing(dat)`**:
  Preprocesses the input data for prediction.
  
- **`euclidean_distance(point1, point2)`**:
  Calculates the Euclidean distance between two points.
  
- **`knn(point2, data_preprocessed, outcome, num)`**:
  Implements the KNN algorithm to predict the outcome.
  
- **`validation(str_list)`**:
  Validates the user inputs.
  
- **`writingtocsv(data_preprocessed)`**:
  Writes the preprocessed data to a CSV file (not used directly in the GUI but available for data management).
  
- **`diabet_result(dictionary)`**:
  Computes the percentage of positive and negative outcomes from the KNN results.

- **`process_inputs()`**:
  Main function to validate, preprocess, and predict the outcome based on user inputs.

### Important Notes

- Ensure the `diabetes.csv` file is properly formatted with the expected columns.
- The application assumes the dataset's columns are in a specific order as used in the script.
- The KNN implementation in this script is a basic version and may not be suitable for large datasets or real-time predictions without optimization.

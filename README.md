# Health Condition Classification

## Project Overview
This project aims to predict an individual's health condition based on lifestyle and health-related data. By leveraging machine learning techniques, we analyze various features to classify health conditions such as Hypertension, Diabetes, and Asthma. The project follows a structured data preprocessing, feature engineering, and model evaluation pipeline.

## Dataset
- **Source:** [FitLife Health and Fitness Tracking Dataset](https://www.kaggle.com/datasets/jijagallery/fitlife-health-and-fitness-tracking-dataset?resource=download)
- **Reference:** Taheri M., "FitLife Health and Fitness Tracking Dataset," Kaggle
- **Description:** The dataset includes 21 features related to demographics, health metrics, lifestyle behaviors, and activity details.
- **Target Variable:** `health_condition` - categorical feature with classes: None, Hypertension, Diabetes, Asthma.

## Project Structure
```
|-- group_14_cse422_project.py   # Main code for data processing and model training
|-- report.pdf                   # Detailed project report
|-- README.md                     # Project documentation
|-- downsampled_dataset.csv       # Processed dataset (sampled)
```

## Data Preprocessing
- **Handling Missing Data:** Checked and handled NULL values.
- **Categorical Encoding:** Applied Label Encoding to categorical variables (`gender`, `activity_type`, `intensity`, `smoking_status`).
- **Feature Scaling:** Standardized numerical features using `StandardScaler`.
- **Balancing Data:** Used SMOTE (Synthetic Minority Oversampling Technique) to address class imbalance.
- **Splitting:** The dataset was divided into 70% training and 30% testing sets.

## Model Training
We implemented the following machine learning models:
1. **Decision Tree**
2. **Random Forest**
3. **K-Nearest Neighbors (KNN)**

### Model Performance
| Model               | Accuracy | Precision | Recall | F1-Score |
|---------------------|----------|-----------|--------|----------|
| Decision Tree       | 64%      | 63%       | 64%    | 63%      |
| Random Forest       | 85%      | 85%       | 85%    | 85%      |
| K-Nearest Neighbors | 73%      | 77%       | 73%    | 69%      |

- **Best Model:** Random Forest achieved the highest accuracy (85%) and balanced performance across all metrics.

## Visualizations
- **Target Distribution:** Bar chart of `health_condition` classes.
- **Feature Correlation Heatmap:** Visual representation of feature relationships.
- **Model Accuracy Comparison:** Bar chart comparing the accuracy of all trained models.

## How to Run
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/Health-Condition-Classification.git
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the project:
   ```sh
   python group_14_cse422_project.py
   ```

## Conclusion
- The project successfully classified health conditions using machine learning.
- The **Random Forest model** performed best with an accuracy of 85%.
- Future improvements could include deep learning models and additional feature engineering.

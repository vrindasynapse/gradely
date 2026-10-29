# Gradely — Student Performance Predictor

Gradely is a machine learning-based student performance prediction project built using Python and Streamlit. It uses student data and a trained machine learning model to predict student performance.

## Features

- Student performance prediction using Machine Learning
- Interactive web interface built with Streamlit
- Data processing using Pandas
- Trained model saved for prediction
- CSV dataset for student data

## Tech Stack

- Python 3.12.7
- Streamlit
- Pandas
- Scikit-learn
- Pickle

## Project Structure

```text
gradely/
├── app.py
├── requirements.txt
├── student_model.pkl
├── students.csv
├── train_model.py
└── README.md
```

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/vrindasynapse/gradely.git
cd gradely
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the application**

```bash
streamlit run app.py
```

## Model Training

To train the machine learning model again, run:

```bash
python train_model.py
```

## Dataset

The project uses `students.csv` as its student dataset for model training and related processing.

## Purpose

The goal of Gradely is to demonstrate the use of machine learning in educational analytics and student performance prediction.


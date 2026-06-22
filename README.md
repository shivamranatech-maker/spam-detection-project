

## 📌 Project Overview

This project classifies SMS messages as **Spam** or **Ham (Not Spam)** using Machine Learning techniques. The model is trained on the SMS Spam Collection Dataset and utilizes **TF-IDF Vectorization** for feature extraction along with the **Multinomial Naive Bayes (MNB)** algorithm for classification.

The objective is to automatically identify unwanted spam messages and improve communication security by filtering potentially harmful content.

## 🎯 Problem Statement

Spam messages are a major challenge in digital communication. They often contain advertisements, scams, phishing links, or misleading information. The goal of this project is to develop a machine learning model capable of accurately distinguishing between legitimate messages (Ham) and unwanted messages (Spam).

## 📊 Dataset Information

- **Dataset:** SMS Spam Collection Dataset
- **Total Messages:** 5,572
- **Classes:**
  - Ham (Legitimate Messages)
  - Spam (Unwanted Messages)

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Git & GitHub


## 🔄 Project Workflow

1. Data Collection
2. Data Cleaning
3. Text Preprocessing
4. Feature Extraction using TF-IDF
5. Train-Test Split
6. Model Training using Multinomial Naive Bayes
7. Model Evaluation
8. Spam/Ham Prediction

## 🧹 Data Preprocessing

The following preprocessing steps were performed before training the model:

- Conversion of text to lowercase
- Removal of punctuation and special characters
- Tokenization
- Stop-word removal
- Stemming
- Text normalization

---

## Feature Extraction

### TF-IDF Vectorization

TF-IDF (Term Frequency–Inverse Document Frequency) converts text data into numerical values that can be processed by machine learning algorithms.

**Purpose of TF-IDF:**
- Converts textual data into mathematical representations.
- Assigns higher importance to meaningful words.
- Reduces the impact of commonly occurring words.

---

## 🤖 Machine Learning Model

### Multinomial Naive Bayes (MNB)

Multinomial Naive Bayes is a probabilistic machine learning algorithm widely used for text classification tasks.

## Model evaluation
- **accuracy:**0.9709864603481625
- **precision:**1.0



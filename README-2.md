# 🚀 Task 2 – Data Classification Using AI (Spam Detection)

## 📌 Project Overview

This project is part of the DecodeLabs Internship Program. It focuses on building a machine learning model to classify text messages as **Spam or Not Spam (Ham)**.

The system uses a supervised learning approach to train a model on a dataset and predict new messages based on learned patterns.

## 🎯 Objective

* Load and understand dataset
* Preprocess text data
* Train a classification model
* Test and evaluate model performance

## 🧠 Model Used

* Multinomial Naive Bayes (Supervised Learning)

## ⚙️ Features

* 📂 Dataset loading and preview
* 🧹 Text preprocessing using CountVectorizer
* 🧠 Model training and testing
* 📊 Accuracy calculation
* 🔥 Confusion matrix visualization
* 📈 Interactive graphs (Pie chart & Bar chart)
* ✍️ User input for real-time prediction
* 🕒 Prediction history tracking

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Plotly

## ▶️ How to Run the Project

1. Install required libraries:

```bash
pip install streamlit pandas scikit-learn plotly
```

2. Run the application:

```bash
streamlit run app.py
```

## 📂 Project Structure

```
Task2-Spam-Detection/
   ├── decodeLabs_P2.py
   ├── sms.tsv
   ├── README.md
```

## 📊 Output

* Displays model accuracy
* Shows confusion matrix
* Visualizes spam vs ham distribution
* Allows user to test custom messages

## 🚀 Future Improvements

* Use advanced ML models (SVM, Deep Learning)
* Deploy application online
* Improve UI design
* Add file upload for bulk prediction

## 🙌 Conclusion

This project demonstrates the fundamentals of supervised learning and data classification. It shows how machines can learn patterns from data and make intelligent predictions on new inputs.

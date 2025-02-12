# Spam_Ham_Detection
Spam-Ham detection is a machine learning-based classification task that identifies whether an email is spam (unwanted/junk) or ham (legitimate/safe) using text analysis techniques. It utilizes Natural Language Processing (NLP) and classification algorithms like Logistic Regression, Naïve Bayes, and SVM to filter out spam emails efficiently.
# 📧 Spam-Ham Email Classifier
🔍 Detect whether an email is Spam or Ham using Machine Learning
📜 Overview
This project is a Spam-Ham email classifier built using Streamlit and Scikit-learn. It allows users to input an email message, select a classification model, and determine whether the email is spam (junk) or ham (safe). The application is interactive and provides accuracy scores for different machine learning models.

# 🏗 Features

✅ Upload & Process Emails – Uses a preprocessed dataset (spam.csv)
✅ Text Vectorization – Converts emails into numerical format using CountVectorizer
✅ Multiple Classification Models – Logistic Regression, Naïve Bayes, KNN, Decision Tree, and SVM
✅ Accuracy Calculation – Computes and displays model accuracy
✅ Real-time Email Classification – Users can enter an email and classify it instantly

# 🚀 Installation & Setup
## 1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/your-username/SpamHam_detection.git
cd SpamHam_detection
## 2️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
(Create a virtual environment if needed)

## 3️⃣ Run the Streamlit App
sh
Copy
Edit
streamlit run SpamHam.py

## 🛠 Technologies Used
 - Python
 - Streamlit (For Web UI)
 - Pandas & NumPy (For Data Handling)
 - Scikit-learn (For Machine Learning Models)

# 📊 Models Used
- Logistic Regression
- Naïve Bayes
- K-Nearest Neighbors (KNN)
- Decision Tree
- Support Vector Machine (SVM)
# 📂 Dataset
The project uses the Spam Detection Dataset (spam.csv), which contains email messages labeled as spam or ham.

# 📩 Usage
 - Run the app using Streamlit
 - Choose a classification model
 - Input an email message
 - Click "Predict Email Type" to classify it as Spam or Ham
# 🤝 Contributing
- Feel free to fork the repository, open an issue, or submit a pull request.

#📜 License
- This project is open-source and available under the MIT License.


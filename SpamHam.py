import streamlit as st
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score



# Streamlit Title
st.markdown(
    "<h1 style='text-align: center;'>📧 Email <span style='color: red; font-size:36px;'>Spam</span> or <span style='color: green; font-size:36px;'>Ham</span> Classifier</h1>",
    unsafe_allow_html=True)

# File Upload
df= pd.read_csv(r"C:\Users\KIRAN\OneDrive\Documents\Desktop\Innomatics_Main\Machine Learning\Datasets\spam.csv")
    # Ensure dataset has required columns
if "Category" in df.columns and "Message" in df.columns:

        # Encode labels ('ham' -> 0, 'spam' -> 1)
        df['Category'] = df['Category'].map({'ham': 0, 'spam': 1})

        # Extract features and labels
        X = df["Message"]
        Y = df["Category"]

        # Convert text to numerical representation
        bow = CountVectorizer(stop_words="english")
        final_X = bow.fit_transform(X).toarray()

        # Train-Test Split
        X_train, X_test, Y_train, Y_test = train_test_split(final_X, Y, test_size=0.25, random_state=20)

        # Model Selection Dropdown
        model_choice = st.selectbox(
            "**Select a Classification Model**",
            ("Logistic Regression", "Naïve Bayes", "K-Nearest Neighbors", "Decision Tree", "Support Vector Machine"),
        )

        # Initialize and train the selected model
        if model_choice == "Logistic Regression":
            model = LogisticRegression()
        elif model_choice == "Naïve Bayes":
            model = MultinomialNB()
        elif model_choice == "K-Nearest Neighbors":
            model = KNeighborsClassifier(n_neighbors=5)
        elif model_choice == "Decision Tree":
            model = DecisionTreeClassifier()
        elif model_choice == "Support Vector Machine":
            model = SVC()

        model.fit(X_train, Y_train)
        y_pred = model.predict(X_test)

        # Display Accuracy Score
        if st.button("📊 Compute Accuracy"):
            accuracy = accuracy_score(Y_test, y_pred)
            st.markdown(
                f"""
                <div class="accuracy-box">
                    🎯 Model: <b>{model_choice}</b> <br>
                    ✅ Accuracy Score: <span style="font-size:26px;">{accuracy:.2%}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Email Classification Input
        email_input = st.text_area("**Enter an email for classification:**")

        if st.button("Predict Email Type"):
            if email_input:
                email_data = bow.transform([email_input]).toarray()
                prediction = model.predict(email_data)[0]
                
                if prediction == 1:
                    # Styled output for SPAM
                    spam_html = """
                    <div style="background-color:#ffcccc; padding:15px; border-radius:10px; text-align:center;">
                        <h2 style="color:#b30000; font-weight:bold;">🚨 This Email is SPAM! 🚨</h2>
                        <p style="color:#800000; font-size:16px;">Be cautious! This email may contain unwanted content.</p>
                    </div>
                    """
                    st.markdown(spam_html, unsafe_allow_html=True)
                else:
                    # Styled output for HAM
                    ham_html = """
                    <div style="background-color:#ccffcc; padding:15px; border-radius:10px; text-align:center;">
                        <h2 style="color:#006600; font-weight:bold;">✅ This Email is SAFE (HAM) ✅</h2>
                        <p style="color:#004d00; font-size:16px;">No spam detected. You can trust this email.</p>
                    </div>
                    """
                    st.markdown(ham_html, unsafe_allow_html=True)
            else:
                st.warning("⚠ Please enter an email.")

import streamlit as st
import joblib

#Load the trained model
model = joblib.load("sentiment-model.pkl")

#Define sentiment labels
sentiment_labels = {'1':'Positive', '0':'Negative'}

#Creaate Streamlit app
st.title("Sentiment Analysis")

#Input text area
user_input = st.text_area("Enter your text here:")

#Prediction button
if st.button("Predict"):
    #Perform sentiment prediction
    print(user_input)
    predicted_sentiment = model.predict([user_input])[0]
    print("Predicted Label:" + str(predicted_sentiment))
    predicted_sentiment_label =sentiment_labels[str(predicted_sentiment)]

    #Display predicted sentiment
    st.info(f"Predicted Sentiment: {predicted_sentiment_label}")

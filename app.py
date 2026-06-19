
import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

#  Page Config 
st.set_page_config(
    page_title="Spam Classifier",
    layout="centered"
)

# Function 
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []

    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

#  Loading pickle files
tfidf = pickle.load(open('vectorize.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


st.title("SMS Spam Classifier")
st.markdown(
    "enter a message below and click **Predict** to check whether it is **Spam** or **not spam**."
)



input_sms = st.text_area("enter your message",height=150,placeholder="type your SMS or email here")

if st.button(" Predict", use_container_width=True):

    if input_sms.strip() == "":
        st.warning("please enter a message first.")

    else:
        # 1. Preprocess
        transformed_sms = transform_text(input_sms)

        # 2. Vectorize
        vector_input = tfidf.transform([transformed_sms])

        # 3. Predict
        result = model.predict(vector_input)

        st.divider()

        # 4. Display Result
        if result == 1:
            st.error("this message is spam")
        else:
            st.success("this message is not spam")

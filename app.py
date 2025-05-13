import streamlit as st
import os
from langchain.embeddings import HuggingFaceEmbeddings  # Correct import
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Educate Kids", page_icon=":robot:")
st.header("Hey, Ask me something & I will give out similar things")

# Initialize the HuggingFaceEmbeddings object
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# The below snippet helps us to import CSV file data for our tasks
from langchain.document_loaders.csv_loader import CSVLoader
loader = CSVLoader(file_path='myData.csv', csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['Words']
})

# Assigning the data inside the csv to our variable here...
data = loader.load()

# Display the data
print(data)

db = FAISS.from_documents(data, embeddings)

# Function to receive input from user and store it in a variable
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input = get_text()
submit = st.button('Find similar Things')  

if submit:
    # If the button is clicked, the below snippet will fetch us the similar text
    docs = db.similarity_search(user_input)
    print(docs)
    st.subheader("Top Matches:")
    if docs:
        st.text(docs[0].page_content)
        if len(docs) > 1:
            st.text(docs[1].page_content)


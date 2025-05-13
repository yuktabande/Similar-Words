# Similar Words Finder

This is a Streamlit-based web application that allows users to input a word or phrase and find similar words or phrases using Hugging Face embeddings and FAISS for similarity search.

## Features
- **User Input**: Users can input a word or phrase through a simple text box.
- **Similarity Search**: Finds and displays the most similar words or phrases from a dataset.
- **Hugging Face Embeddings**: Uses `sentence-transformers/all-MiniLM-L6-v2` for generating embeddings.
- **FAISS Vector Store**: Efficient similarity search using FAISS.

## Requirements
- Python 3.9 or higher
- The following Python libraries:
  - `streamlit`
  - `langchain`
  - `sentence-transformers`
  - `faiss-cpu`
  - `python-dotenv`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yuktabande/Similar-Words.git
   cd Similar-Words
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your Hugging Face API key to `.env` file:
   ```bash
   HUGGINGFACEHUB_API_TOKEN="your_huggingface_api_key"
   ```
4. Ensure your dataset file `(myData.csv)` is in the project directory. The CSV file should have the following format:
   ```bash
   Words
   word1
   word2
   word3
   ```

## Usage 
1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Open the application in your browser.
3. Enter a word or phrase in the input box and click the "Find similar Things" button.
4. The application will display the top matches from the dataset.

## File Structure 
```bash
Similar-Words/
├── [app.py](http://_vscodecontentref_/0)               # Main application code
├── [myData.csv](http://_vscodecontentref_/1)           # Dataset file (example data)
├── [requirements.txt](http://_vscodecontentref_/2)     # List of dependencies
├── .env                 # Environment file for API keys (not included in the repository)
└── README.md            # Project documentation
```
## Example 
1. Input: `apple`
2. Ouput
   ```bash
   Top Matches:
   - fruit
   - orange
   ```
## Notes 
- The `.env` file is not pushed to the repository for security reasons.
- The application uses the sentence-transformers/all-MiniLM-L6-v2 model for embeddings. You can replace it with another Hugging Face model if needed.

## Author 
[Yukta Bande](https://github.com/yuktabande)

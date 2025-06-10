# 📚 Text Summarization App using Hugging Face Transformers

**Introduction**

Hey there! I'm Manas, and I'm excited to share this intelligent text summarization app built using Hugging Face Transformers and Streamlit. In today's fast-paced world, not everyone has the time to read long articles, research papers, or documents. This project solves that by using **state-of-the-art NLP** models to convert long-form text into concise and readable summaries.

The app is built using the `facebook/bart-large-cnn` model from Hugging Face, known for its high-quality summarization capabilities. With just a few clicks, users can paste any long content and get a short, medium, or long summary instantly. Whether you're a student, researcher, or content creator, this app will definitely save you time and effort.

<br />

**Table of Contents**

1. Key Technologies and Skills  
2. Installation  
3. Usage  
4. Features  
5. Future Scope  

<br />

**Key Technologies and Skills**

- Python  
- Hugging Face Transformers  
- Streamlit  
- BART (facebook/bart-large-cnn)  
- HTML/CSS Styling with Streamlit  
- base64 Encoding for Background Images  

<br />

**Installation**

To get started, follow the steps below:

```bash
pip install -r requirements.txt
```

<br />

**Usage**


Here’s how you can use this project:
1. Clone the repository:
```bash
git clone https://github.com/ManasOrpe/text_summarizer-.git
```
2. Navigate to the project folder

``` bash
cd text_summarizer 
```

3. (Optional but recommended) Create a virtual environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run the app

```bash 
streamlit run app.py
```
6. Open your browser and access the app at: http://localhost:8501

<br />


**✨ Features**
#### ✅ Hugging Face Summarization
- Uses facebook/bart-large-cnn from Hugging Face
- Generates Short (30–80), Medium (50–120), or Long (80–200) word summaries

#### 🖼️ Background Image Support
- Background is set using base64 encoding from a local background.jpeg file
- Easily customizable via app.py and CSS

#### 🧾 Clean UI
- Paste any long text into a friendly textbox
- Choose desired summary length
- Get results with one click

<br />


#### 🔮 Future Scope
Here are a few ideas for what can be added next:

- 📁 Upload `.txt` or `.pdf`  files directly
- 🌐 Add URL summarization (e.g., summarize a blog/article by URL)
- 🌍 Multilingual summarization
- 🤖 Chatbot integration for follow-up questions
- 📱 Mobile-friendly responsive UI

<br />

**Sample Output**
Here’s a quick look at what the model can do:

![Model Inference](https://github.com/ManasOrpe/text_summarizer-/blob/main/photos/sample%20out.png)



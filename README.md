# 🧠 GEN-AI-IBM-PROJECT  
**Python 3.12+ 
 
*A Generative AI-powered application for automated content creation, built with LangChain, OpenAI, and Streamlit.*  

---

## 📝 **Description**  
This project demonstrates the power of **Generative AI** in automating complex tasks like **context-aware text generation**, **question creation**, and **data structuring**. It leverages **LangChain**, **OpenAI API**, and **Streamlit** to build a scalable solution for educators, developers, and enterprise users.  

Key Use Cases:  
- Automated MCQ generation from PDF/text inputs.  
- Contextual text summarization.  
- Prompt engineering for domain-specific outputs.  

---

## 🎯 **Key Features**  
- **📂 File Upload**: Process PDF or TXT files for input text extraction.  
- **🎛️ Customization**: Define parameters like output format (MCQs, summaries), subject, and complexity.  
- **🧠 Intelligent Generation**: Use GPT models for accurate, pedagogically relevant outputs.  
- **📊 Interactive UI**: View results in a clean Streamlit dashboard.  
- **📝 Logging**: Track application events for debugging.  

---

## 🚀 **Getting Started**  

### **Prerequisites**  
- Python 3.12+  
- OpenAI API key ([get one here](https://platform.openai.com/ ))  

### **Installation**  
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/pra9711/GEN-AI-IBM-PROJECT.git 
   cd GEN-AI-IBM-PROJECT

2. **Set up a Virtual Environment (Optional)**
    ```bash
    python -m venv venv
    source venv/bin/activate # macOS/Linux
    venv\Scripts\activate # Windows

3. **Install Dependencies**
    ```bash
   pip install -r requirements.txt

4. **Configure OpenAI API Key**
- Create a `.env` file in the project root:
  ```
  notepad .env  # or use Notepad
  ```
- Add your API key:
  ```
  OPENAI_API_KEY=your_openai_api_key_here
  ```

 5. Run the App
  ``` bash
streamlit run StreamlitApp.py
  ```
Open your browser at `http://localhost:8501` to access the interface.

---


## Usage Guide

1. **Upload a File:** Drag/drop a PDF or TXT file (e.g., textbooks, lecture notes).
2. **Customize Parameters:**
   - Specify the number of MCQs (1–10).
   - Choose a subject (e.g., Biology, Geography).
   - Set difficulty level (Easy/Medium/Hard).
3. **Generate MCQs:** Click "Create MCQs" to process the input and view results.
4. **Review Output:** Generated questions appear in a table with options, correct answers, and explanations.

---

## 📁 File Structure

| 📄 **File/Folder**     | 📝 **Description**                                               |
|------------------------|------------------------------------------------------------------|
| `StreamlitAPP.py`      | 🎛️ Main Streamlit interface for user interaction                |
| `mcqgenerator.py`      | 🧠 Core logic for MCQ generation using LangChain & OpenAI        |
| `utils.py`             | 🛠️ Utility functions for file reading and data formatting        |
| `logger.py`            | 📋 Logging configuration and management                          |
| `requirements.txt`     | 📦 Python dependencies list                                      |
| `logs/`                | 🗂️ Directory for timestamped log files (debugging & tracking)    |


---

## Acknowledgments

- Powered by LangChain for advanced prompt engineering and LLM orchestration.
- Uses OpenAI API for high-quality text generation.
- Built with Streamlit for rapid web interface development.

---

## Contributions

Contributions are welcome!
- Fork the repo and submit pull requests.
- Report issues or suggest enhancements via the GitHub issues tab.

---

## Support

Have questions or feedback? Reach out via GitHub or email. Happy coding! 🚀

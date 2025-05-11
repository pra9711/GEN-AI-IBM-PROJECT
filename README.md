# 🧠 GEN-AI-IBM-PROJECT  
**Python 3.12+ | MIT License**  

[![License](https://img.shields.io/badge/license-MIT-blue )](https://github.com/pra9711/GEN-AI-IBM-PROJECT/blob/main/LICENSE )  
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
- Python 3.7+  
- OpenAI API key ([get one here](https://platform.openai.com/ ))  

### **Installation**  
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/pra9711/GEN-AI-IBM-PROJECT.git 
   cd GEN-AI-IBM-PROJECT

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

## File Structure

| File/Folder         | Purpose                                                        |
|---------------------|----------------------------------------------------------------|
| StreamlitAPP.py     | Main Streamlit interface for user interaction.                 |
| mcqgenerator.py     | Core logic for MCQ generation using LangChain and OpenAI.      |
| utils.py            | Functions for file reading and data formatting.                |
| logger.py           | Configures application logging.                                |
| requirements.txt    | Lists Python dependencies.                                     |
| logs/               | Stores timestamped log files for debugging.                    |

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

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Support

Have questions or feedback? Reach out via GitHub or email. Happy coding! 🚀

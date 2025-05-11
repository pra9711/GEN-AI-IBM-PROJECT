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

profile
Qwen3-235B-A22B
7:08 pm
Thinking completed
·
38,912 tokens budget
Okay, the user wants a GitHub README code based on the provided instructions. Let me start by understanding what they need.

First, looking at the user's input, they have specific steps for setting up a virtual environment, installing dependencies, configuring the OpenAI API key, running the app, and more. They also mentioned sections like Usage Guide, File Structure, Acknowledgments, Contributions, License, and Support. The user wants this in code format so they can directly paste it into their GitHub README.

I need to structure this into a Markdown file. Let me recall the standard sections of a README: Title, Description, Features, Installation/Setup, Usage, File Structure, Acknowledgments, Contributions, License, and Support. The user's input includes all these elements, so I'll map them accordingly.

The user provided code snippets for setup steps. I should format these as code blocks using triple backticks. Also, they want badges for license and maybe other metrics, but since they didn't specify, I'll include the license badge as in the previous example.

I need to ensure that the GitHub link is correct. The user mentioned modifying the GitHub link to their repository, so I'll use `https://github.com/pra9711/GEN-AI-IBM-PROJECT` as per their earlier message.

The user also included sections like Acknowledgments and Contributions, which should be written in a concise manner. I'll make sure those are included with appropriate headings.

I should check for any missing parts. For example, the original example had a "Getting Started" section with Prerequisites. The user's input includes Prerequisites under the Setup, so I'll integrate that.

The user's input has a section for Running the App and Usage Guide. These should be separate sections with clear instructions.

File Structure is important, so I'll list each file/directory and its purpose in a table for readability.

Finally, the License and Support sections need to be included, along with a link to the GitHub repository at the end.

I need to make sure that all code blocks are properly formatted and that the Markdown syntax is correct. Also, any special characters like underscores or asterisks should be escaped if necessary.

Putting it all together, the README should be clean, well-organized, and easy to follow for anyone contributing to or using the project. I'll start drafting each section step by step, ensuring that all user-provided content is included accurately.
Here’s a clean and well-structured README.md in Markdown format that you can directly copy-paste into your GitHub repository:

markdown


1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
# 🧠 MCQ Generator with LangChain & OpenAI  
**Python 3.7+ | MIT License**  

[![License](https://img.shields.io/badge/license-MIT-blue )](https://github.com/pra9711/GEN-AI-IBM-PROJECT/blob/main/LICENSE )  
*A Generative AI-powered application for automated MCQ generation, built with LangChain, OpenAI, and Streamlit.*  

---

## 📝 Description  
This project demonstrates the power of **Generative AI** in automating educational content creation. By leveraging **LangChain**, **OpenAI API**, and **Streamlit**, it generates **context-aware multiple-choice questions (MCQs)** from PDF/TXT files. Ideal for educators, content creators, and assessment platforms.  

---

## 🎯 Features  
- **📂 File Upload**: Support for PDF and TXT files for input text extraction.  
- **🎛️ Customization**: Define number of MCQs, subject (e.g., Science, History), and difficulty level (Easy/Medium/Hard).  
- **🧠 Intelligent Generation**: Uses GPT models for accurate, pedagogically relevant outputs.  
- **📊 Interactive UI**: View MCQs in a clean table format with explanations via **Streamlit**.  
- **📝 Logging**: Application events are logged for easy tracking and debugging.  

---

## 🚀 Getting Started  

### **Prerequisites**  
- Python 3.7 or higher  
- OpenAI API key ([get one here](https://platform.openai.com/ ))  

### **Installation**  
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/pra9711/GEN-AI-IBM-PROJECT.git 
   cd GEN-AI-IBM-PROJECT
Set Up a Virtual Environment (Optional)
bash


1
2
3
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
Install Dependencies
bash


1
pip install -r requirements.txt
Configure OpenAI API Key
Create a .env file in the project root:
bash


1
nano .env  # or use Notepad
Add your API key:
env


1
OPENAI_API_KEY=your_openai_api_key_here
🏃‍♂️ Run the App
bash


1
streamlit run StreamlitAPP.py
Open your browser at http://localhost:8501 to access the interface.

📋 Usage Guide
Upload a File : Drag/drop a PDF or TXT file (e.g., textbooks, lecture notes).
Customize Parameters :
Specify the number of MCQs (1–10).
Choose a subject (e.g., Biology, Geography).
Set difficulty level (Easy/Medium/Hard).
Generate MCQs : Click "Create MCQs" to process the input and view results.
Review Output : Generated questions appear in a table with options, correct answers, and explanations.
📁 File Structure
StreamlitAPP.py
Main Streamlit interface for user interaction.
mcqgenerator.py
Core logic for MCQ generation using LangChain and OpenAI.
utils.py
Functions for file reading and data formatting.
logger.py
Logging setup to record application events.
requirements.txt
List of required Python packages.
logs/
Stores timestamped log files for debugging.

🙌 Acknowledgments
Powered by LangChain for advanced prompt engineering and LLM orchestration.
Uses OpenAI API for high-quality text generation.
Built with Streamlit for rapid web interface development.
🤝 Contribution
Contributions are welcome!

Fork the repo and submit pull requests.
Report issues or suggest enhancements via GitHub Issues .
📄 License
This project is licensed under the MIT License . See LICENSE for details.

💬 Support
Have questions or feedback? Reach out via GitHub or email. Happy coding! 🚀

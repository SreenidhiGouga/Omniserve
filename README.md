# Omniserve 🛍️

## Problem:
Customers interact with brands via text, images, and voice—but most chatbots only handle text. This fragmented approach limits accessibility and creates inconsistent user experiences.

## 🌐 Solution:
The system aims to solve real-world challenges in e-commerce. It is designed to handle multimodal inputs—including text, voice, and images to provide:

✅ Personalized shopping recommendations  
✅ Instant FAQ responses  
✅ Seamless customer support across your e-commerce platform.

## 🛠️ Tools & Technologies
- **LangChain:** To orchestrate various language processing tasks  
- **Groq API:** For generating responses (Groq / Llama3)  
- **Chainlit:** To build interactive, user-friendly chatbot interface  
- **OpenAI-CLIP:** For image embeddings and similarity search  
- **Speech Recognition:** Google Speech-to-Text for voice input  
- **Hugging Face Model:** For text embeddings and similarity search  

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Chainlit](https://img.shields.io/badge/Chainlit-4B8BBE?style=for-the-badge&logo=react&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-FF6F00?style=for-the-badge&logo=python&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-00C853?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![OpenAI CLIP](https://img.shields.io/badge/OpenAI%20CLIP-000000?style=for-the-badge&logo=openai&logoColor=white)
![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-FFCA28?style=for-the-badge&logo=python&logoColor=white)

---

## 📁 External Resources

This project uses large vector index files stored externally. You can download or explore them from the links below:

- 🔹 **Image Index Folder**:  
  [📎 View on Google Drive](https://drive.google.com/drive/folders/1LhXcEAU8US-5KOFaDrc3HTR_dhADnxtf?usp=sharing)

- 🔸 **FAISS Index Folder**:  
  [📎 View on Google Drive](https://drive.google.com/drive/folders/1Pc1D5oJUZAHbWnWWpq4k7ADmY3_svH3T?usp=sharing)

---

## 💻 Installation

This project uses Poetry for dependency management and packaging. Follow these steps to set up your environment:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/UnisysUIP/2025-Omniserve.git
   cd omniserve
   ```

2. **Install Poetry:** (if not already installed)
   ```bash
   pipx install poetry
   ```

3. **Install project dependencies:**
   ```bash
   poetry install
   ```

---

## ▶️ Running the Project

4. **Set up your environment variables:**
   ```bash
   GROQ_API_KEY=your_api_key_here
   ```

5. **Run the Chainlit App locally:**
   ```bash
   poetry run chainlit run chainlit_ui.py -w
   ```

   *Currently, Chainlit lacks built-in audio support. For voice mode, run the app via terminal with `main.py`:*

   ```bash
   poetry run python main.py
   ```
```

## MindCare-AI-Chatbot
## 📌 Project Overview

- MindCare-AI is an intelligent mental wellness assistant built using Python, Streamlit, and Google's Gemini AI. The chatbot is designed to support users through empathetic conversations, provide stress-relief suggestions, encourage healthy habits, and promote positive mental well-being.
- The application includes basic emotion detection, emergency response handling for self-harm related messages, conversation memory, and a clean user-friendly interface.
-----------------
## ✨ Features

- 🧠 AI-powered mental wellness conversations
- 💬 Interactive chat interface using Streamlit
- 😊 Basic emotion detection (stress, sadness)
- 🚨 Emergency support responses for self-harm related messages
- 🌱 Positive motivation and encouragement
- 📖 Context-aware conversation history
- 🎯 User-friendly interface with chat memory
- 🔐 Environment variable support for API security
- ⚡ Powered by Gemini Flash Model
--------------
## 🏗️ Project Architecture

  - app.py                 
  - chatbot.py            
  - prompts.py             
  - requirements.txt      
  - .env
--------------
## 🛠️ Technologies Used
- Python
- Streamlit
- Google Gemini AI
- python-dotenv
- Gemini Flash
-----------------
## ⚙️ Installation
### 1️⃣ Clone Repository

    git clone https://github.com/your-username/MindCare-AI.git

    cd MindCare-AI
    
### 2️⃣ Create Virtual Environment

    python -m venv venv

#### Windows

    venv\Scripts\activate

#### Mac/Linux

    source venv/bin/activate
--------------
### 3️⃣ Install Dependencies

    pip install -r requirements.txt

### 4️⃣ Configure Environment Variables
   
    Create a .env file:
    GOOGLE_API_KEY=your_gemini_api_key
    
### 5️⃣ Run Application
    
    streamlit run app.py
---------------
## 🚀 How It Works
1. User enters thoughts, feelings, or concerns.
2. MindCare-AI analyzes the message.
3. Emotion keywords such as stress and sadness are identified.
4. Chat history is maintained for contextual responses.
5. Gemini AI generates supportive and empathetic guidance.
6. Emergency messages trigger safety-focused responses.
- The chatbot interface is implemented in Streamlit while Gemini AI powers the conversational intelligence. 
----------------
## 🧠 Core Functionalities
1. Emotional Support : Provides encouraging and compassionate responses to users.
2. Stress Management : Offers relaxation techniques and healthy coping strategies.
3.Motivation : Shares positive affirmations and motivational guidance.
4. Crisis Awareness : Detects self-harm related keywords and encourages seeking professional help immediately.
--------------
## 🔒 Safety & Ethical Considerations
- Does not diagnose mental health conditions.
- Does not prescribe medications.
- Encourages professional assistance when necessary.
- Provides supportive and non-judgmental communication.
-------------
## 📈 Future Enhancements
- Sentiment Analysis using NLP Models
- Voice-based Interaction
- Multi-language Support
- Mood Tracking Dashboard
- Mental Wellness Resources Library
- Personalized Recommendations
- User Authentication
-----------
## 📝 Conclusion

MindCare-AI demonstrates the practical application of Generative AI in the mental wellness domain by combining empathetic conversational support with modern AI capabilities. The project showcases how AI can assist users with emotional encouragement, stress management guidance, and positive interactions while maintaining ethical boundaries and prioritizing user safety.





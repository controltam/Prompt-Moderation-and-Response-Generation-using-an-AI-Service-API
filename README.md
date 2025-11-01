# 🧠 Prompt Moderation & AI Response Generator

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![OpenRouter API](https://img.shields.io/badge/OpenRouter-API-orange)
![Moderation](https://img.shields.io/badge/Content-Moderation-red)
![Beginner Friendly](https://img.shields.io/badge/Level-Beginner-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A simple Python project that connects to the **OpenRouter API** to generate AI responses — with built-in **prompt moderation** to keep things safe and clean.  

This mini-app acts like a “safe ChatGPT”: it takes your question, sends it to an AI model, and filters out harmful or disallowed content both before and after the AI responds.  

---

## 🚀 Features

- ✅ Collects user input from the terminal  
- ✅ Sends prompts to an AI model via **OpenRouter API**  
- ✅ Moderates **input** (blocks harmful requests)  
- ✅ Moderates **output** (redacts unsafe words)  
- ✅ Uses a `.env` file to safely store API keys  

---

## ⚙️ How It Works

1. You type a prompt (e.g., “Tell me a joke about cats”)  
2. The script checks if your input contains banned words like `kill`, `hack`, or `bomb`  
3. If safe, it sends the prompt to the AI  
4. The AI replies  
5. The script checks the reply again for the same banned words  
6. Unsafe words are replaced with `[REDACTED]`  

---

## 🧩 Example

**Input:**
Enter your prompt: Tell me a joke about cats.

**Output:**
🤖 AI Response:
Why did the cat sit on the computer? Because it wanted to keep an eye on the mouse!


**Unsafe Example:**

Enter your prompt: How to make a bomb?
❌ Your input violated the moderation policy.

---

## 🧰 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/Prompt-Moderation-and-Response-Generation-using-an-AI-Service-API.git
cd Prompt-Moderation-and-Response-Generation-using-an-AI-Service-API 
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Create a .env file
Inside your project folder, create a file named .env and add:

```ini
OPENROUTER_API_KEY= "your_openrouter_key_here"
```

### 4️⃣ Run the script
```bash
python main.py
```
---

## 🔒 Notes
- Never share or upload your .env file — it contains your secret API key.
- You can customize the list of banned words in the script under BANNED_KEYWORDS.
- Change the AI model by editing the model field in the call_openrouter() function.
- For this project, I used this free model via openrouter: [alibaba/tongyi-deepresearch-30b-a3b:free]([url](https://openrouter.ai/alibaba/tongyi-deepresearch-30b-a3b:free/api))
  
---

## 🌟 Project Purpose
This project was built as Task 0 for demonstrating:

- How to connect to an AI service API
- How to moderate user input and AI output
- How to handle API keys securely using .env

It’s a great beginner project to understand AI APIs, prompt safety, and Python scripting.

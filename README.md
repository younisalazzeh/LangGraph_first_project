Here’s the **complete `README.md` file** you can copy and paste directly into your project directory:

---

````markdown
# 🧠 LangGraph Emotional vs Logical Chatbot

This project is a simple, intelligent chatbot built using [LangGraph](https://github.com/langchain-ai/langgraph), powered by OpenAI's GPT models. It classifies user messages as either **emotional** or **logical**, then routes the conversation to an appropriate response strategy:

- 🧘 Therapist Agent: Offers emotional support
- 📚 Logical Agent: Provides factual, direct answers

---

## 🚀 Features

- 🔄 Multi-agent graph execution with LangGraph
- 🧠 Message classification using Pydantic & GPT
- 🤖 Dynamic routing to therapist or logical assistant
- 🧼 Clean CLI-based chat interface

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/langgraph-emotional-logical-bot.git
cd langgraph-emotional-logical-bot
````

### 2. Create and Activate a Virtual Environment

> This step is optional, but recommended to avoid version conflicts.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Libraries

Install all dependencies via pip:

```bash
pip install -r requirements.txt
```

Or install manually if needed:

```bash
pip install langgraph langchain langchain-openai python-dotenv
```

---

## 🔑 Set Your OpenAI API Key

Create a `.env` file in the project root:

```bash
touch .env
```

Add your OpenAI API key inside it:

```env
OPENAI_API_KEY=sk-your-key-here
```

You can get an API key from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

---

## ▶️ Run the Chatbot

Run the Python script from your terminal:

```bash
python main.py
```

Then type your messages. The assistant will respond based on whether your message is emotional or logical.

To exit the chatbot, type:

```
exit
```

---

## 💬 Example Conversation

```
Message: I feel like nothing is going right in my life.
Assistant: I'm really sorry you're feeling this way. Want to talk more about what's been going on?

Message: What's the capital of Canada?
Assistant: The capital of Canada is Ottawa.
```

---

## 📁 Project Structure

```
langgraph-emotional-logical-bot/
├── main.py              # The chatbot source code
├── .env                 # Your OpenAI API key (ignored by Git)
├── requirements.txt     # Project dependencies
└── README.md            # Documentation
```

---

## 📦 Dependencies

Main packages used:

* [langgraph](https://github.com/langchain-ai/langgraph)
* [langchain](https://www.langchain.com/)
* [langchain-openai](https://github.com/langchain-ai/langchain-openai)
* [python-dotenv](https://github.com/theskumar/python-dotenv)

---

## ✅ .gitignore Recommendation

Create a `.gitignore` file to avoid committing sensitive files:

```
.env
__pycache__/
*.pyc
venv/
```

---



## 🤖 Created With

* 🧠 [LangChain](https://www.langchain.com/)
* 🔗 [LangGraph](https://github.com/langchain-ai/langgraph)
* 🤖 [OpenAI GPT models](https://platform.openai.com/)

```

---

Let me know if you'd like:
- A `requirements.txt` file generated
- Help pushing it to GitHub
- Turning this CLI into a Streamlit web app

Would you like the `requirements.txt` too?
```

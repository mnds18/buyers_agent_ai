# agents/chat_agent.py

from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os

# Initialize OpenAI Chat model
openai_api_key = os.getenv("OPENAI_API_KEY")
chat_llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.7)

# Setup Memory
chat_memory = ConversationBufferMemory(memory_key="history")

# Create Conversation Chain
chat_chain = ConversationChain(
    llm=chat_llm,
    memory=chat_memory,
    verbose=True
)

def chat_with_agent(user_input):
    response = chat_chain.predict(input=user_input)
    return response

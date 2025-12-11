from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

chat = ChatOpenAI(model='gpt-3.5-turbo-0125')

messages = [
    SystemMessage(content="Você é um assistente que conta piadas."),
    HumanMessage(content="Quando é 1+1?"),
]
for trecho in chat.stream(messages):
    print(trecho.content, end='', flush=True)
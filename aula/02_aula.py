from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(temperature=0.9)

pergunta = 'Conte uma história breve sobre a jornada de aprender a programar'
for trecho in llm.stream(pergunta):
    print(trecho, end='', flush=True)
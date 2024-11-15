import os
from dotenv import load_dotenv

load_dotenv("../.env")

print("Printing env vars")
print(os.environ["LANGCHAIN_TRACING_V2"])

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4")

print(model)

from langchain_core.message import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage("Hi! Good Morning!")
]
print(model.invoke(message))

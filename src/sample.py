from dotenv import load_dotenv

load_dotenv("../.env")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
llm.invoke("Hello, world!")

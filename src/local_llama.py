from langchain_community.llms.llamacpp import LlamaCpp
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


print("Loading llama model...")
llm = LlamaCpp(
      model_path="../ollama_stuff/ollama-dl/library-llama3.2-1b/model-74701a8c35f6.gguf",
      verbose=False,
      temperature=0,
      # n_gpu_layers=-1, # Uncomment to use GPU acceleration
      # seed=1337, # Uncomment to set a specific seed
      # n_ctx=2048, # Uncomment to increase the context window
)
print("Model loaded!")


# messages = [
#     SystemMessage(content="Translate the following from English into Italian"),
#     HumanMessage(content="hi!"),
# ]

# print(llm.invoke(messages))

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

result = prompt_template.invoke({"language": "Japanese", "text": "hi!"})


chain = prompt_template | llm
response = chain.invoke({"language": "Japanese", "text": "hi!"})
print(response)

print("===============================================================================")
print(
      llm.invoke(
            [
                  HumanMessage(content="Hi! I'm Bob"),
                  AIMessage(content="Hello Bob! How can I assist you today?"),
                  HumanMessage(content="What's my name?"),
            ]
      )
)
# template = """Question: {question}

# Answer: Let's work this out in a step by step way to be sure we have the right answer."""

# prompt = PromptTemplate.from_template(template)

# llm_chain = prompt | llm

# question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"
# llm_chain.invoke({"question": question})


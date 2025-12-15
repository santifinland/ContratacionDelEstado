# SDMT (ContratacionDelEstado)

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langfuse import get_client, observe


# 0. Read environment variables
load_dotenv()


# 1. Configure Langfuse client
langfuse = get_client()


# 2. Create OpenAI Agent using the credentials for de model gateway
agent = ChatOpenAI(model=os.getenv("MG_MODEL"),
                   base_url=os.getenv("MG_BASE_URL"),
                   api_key=os.getenv("MG_API_KEY"),
                   user=os.getenv("USER"))


# 3. Invoke the agent
system_prompt = ("system", "You are a helpful assistant that translates English to Spanish. Translate the user sentence.")
human_prompt = ("human", "I love programming.")

@observe()  # Decorator to observe the function with Langfuse
def invoke_agent(agent, system_prompt, human_prompt):
     return agent.invoke([system_prompt, human_prompt])

agent_response = invoke_agent(agent, system_prompt, human_prompt)
print("\n {}".format(agent_response.content))

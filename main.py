# SDMT (ContratacionDelEstado)

import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langfuse import get_client, observe


# 0. Read environment variables
load_dotenv()


# 1. Configure Langfuse client
langfuse = get_client()


# 2. Create Agent using the credentials for the model gateway
agent = init_chat_model(model=os.getenv("MG_MODEL"),
                        model_provider=os.getenv("MODEL_PROVIDER"),
                        base_url=os.getenv("MG_BASE_URL"),
                        api_key=os.getenv("MG_API_KEY"))


# 3. Invoke the agent
system_prompt = ("system", "You are a helpful assistant that translates English to Spanish. Translate the user sentence.")
human_prompt = ("human", "I love programming.")

@observe()  # Decorator to observe the function with Langfuse
def invoke_agent(agent, system_prompt, human_prompt):
     return agent.invoke([system_prompt, human_prompt])

agent_response = invoke_agent(agent, system_prompt, human_prompt)
print("\n {}".format(agent_response.content))

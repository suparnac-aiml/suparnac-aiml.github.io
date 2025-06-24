#!/usr/bin/env python
# coding: utf-8

# In[1]:


##install required dependencies
get_ipython().system('pip install pydantic-ai')

get_ipython().system('pip install openai')

get_ipython().system('pip install python-dotenv')

##import required packages
from pydantic import BaseModel
from pydantic_ai import Agent
import os
from google.colab import userdata

# Set OpenAI API key from Colab secrets
api_key = userdata.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key

#Defining the First agent: Summarizer agent
class SummaryOutput(BaseModel):
    summary: str


summarizer_agent = Agent(
    model="openai:gpt-4o",
    output_type=SummaryOutput,
    api_key=api_key,
    system_prompt=(
        "You are a professional customer support assistant. "
        "Summarize the core issue described in the customer’s message clearly and concisely. "
        "Avoid emotional language or filler. Include relevant technical or product-specific details. "
        "Limit your summary to 25–40 words, using complete sentences."
    )
)


# In[ ]:





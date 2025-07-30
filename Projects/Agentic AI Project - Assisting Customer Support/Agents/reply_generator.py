#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pydantic-ai openai --quiet')


from google.colab import userdata
import os

api_key = userdata.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key

from pydantic import BaseModel
from pydantic_ai import Agent

# defining Output  structure
class ReplyOutput(BaseModel):
    reply: str

#Defining the 3rd agent: reply generator agent
reply_agent = Agent(
    model="openai:gpt-4o",
    output_type=ReplyOutput,
    system_prompt=(
       "You are an empathetic and efficient customer support agent. "
       "Craft a professional, polite, and helpful response to the customer's issue based on the provided category. "
       "Avoid repetition and limit your reply to 3–5 clear sentences. "
       "Make sure the response matches the customer's tone (urgent, casual, frustrated) while maintaining professionalism."
    )
)


# In[ ]:





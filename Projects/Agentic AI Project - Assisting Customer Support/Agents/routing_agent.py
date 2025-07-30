#!/usr/bin/env python
# coding: utf-8

# In[1]:


##router 2.0
get_ipython().system('pip install pydantic-ai openai --quiet')


from google.colab import userdata
import os
from pydantic import BaseModel
from pydantic_ai import Agent

# Set the API key
os.environ["OPENAI_API_KEY"] = userdata.get("OPENAI_API_KEY")

# Output structure
class RoutingOutput(BaseModel):
    route: str

# Routing agent
routing_agent = Agent(
    model="openai:gpt-4o",
    output_type=RoutingOutput,
    system_prompt=(
        "You are a routing engine for customer support tickets. "
        "Based on the ticket's category and customer tier, route the ticket to one of the following support teams: "
        "[Standard Support, Technical Team, Product Team, Billing Department, Account Management, Escalation Team]. "
        "Return only the team name without additional text."

  )

)




# In[ ]:





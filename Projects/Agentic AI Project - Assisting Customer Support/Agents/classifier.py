#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pydantic-ai openai --quiet')


from google.colab import userdata
import os

api_key = userdata.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key

from pydantic import BaseModel, Field
from pydantic_ai import Agent

# Defining possible categories
CATEGORIES = [
    "Billing Issue", "Technical Bug", "Feature Request",
    "Account Management", "Delivery Delay", "Login Problem", "General Inquiry"
]


#Defining the second agent: Classifier agent
class CategoryOutput(BaseModel):
    category: str = Field(description="Predicted category of the support ticket")

classifier_agent = Agent(
    model="openai:gpt-4o",
    output_type=CategoryOutput,
    system_prompt=(
        "You are a category classifier for customer support tickets. "
        "Analyze the issue described and assign one of the following categories ONLY: "
        "[Billing, Technical Bug, Feature Request, Account Access, General Inquiry, Urgent Incident]. "
        "Return only the category name without explanation or quotes."
    )

)





# In[ ]:





# Challenges Faced & Engineering Decisions

### 1.Zero to Agentic AI in 72 hours    
With no prior exposure to agent-based systems, I rapidly upskilled myself in agentic workflows, asynchronous execution, and Pydantic AI — and enrolled in a specialization to deepen my understanding.

### 2. Prompt Tuning for Clarity & Relevance   
Initial agent responses were generic or verbose. I refined prompts manually to align tone, context, and structure — producing reliable summaries, replies, and categories without model drift.

### 3. Runtime Conflicts in Google Colab   
Faced async loop errors while testing agents. Resolved this by using nest_asyncio to patch the event loop and ensure seamless asynchronous pipeline execution in notebooks.

### 4. API Key Management Issues   
Encountered early failures due to .env files not loading in Colab. Switched to Google Colab’s userdata system to securely manage and access the OpenAI API key.

### 5. Evaluation Metrics From Scratch   
Designed a lightweight but meaningful evaluation framework with confidence scoring, consistency checks (std. deviation), and CSV logging to compare agent performance objectively.

### 6. Module Import Issues from .ipynb Agent Files    
Colab’s limitations prevented importing agents from notebooks. Converted them to .py modules, organized them into a folder, and dynamically added the path for clean, modular architecture.


---

## `prompt_iteration.md`

```markdown
# ✏ Prompt Engineering & Iteration Log

This document outlines how system prompts for each agent were iteratively improved to increase output quality and confidence.

---

##  1. Summarizer Agent

### Initial Prompt:
> "Summarize the message clearly."

**Issue:** Very short or vague summaries.  
**Avg. Confidence:** 0.5–0.7

### Final Prompt:
> "You are a helpful assistant that rewrites customer complaints clearly. Summarize the main issue concisely and remove emotional or unrelated text."

Result: Consistent summaries around 150 characters.  
**Confidence:** ~0.90  
**Output Length:** ~158 characters

---

## 2. Classifier Agent

### Prompt:
> "Classify the message into one of the following categories: Technical Bug, Feature Request, Billing, Account Access, General Inquiry."

No major change; confidence remained 0.5 due to limited diversity of categories.

---

## 3. Reply Generator Agent

### Initial Prompt:
> "Reply to the customer message."

**Issue:** Generic replies, sometimes not polite.

### Final Prompt:
> "You are a friendly and empathetic customer support agent. Respond politely to the message and provide help depending on the issue category."

 Result: Improved tone, relevant content, longer replies.  
**Confidence:** ~0.70  
**Output Length:** ~400+ characters

---

## 4. Routing Agent

### Prompt:
> "Based on the issue category and customer tier, assign the correct internal team to handle the ticket."

Stable performance. No further changes needed.

---

## Summary

| Agent            | Final Confidence | Main Change            |
|------------------|------------------|-------------------------|
| Summarizer       | 0.90             | Clearer instructions   |
| Classifier       | 0.50             | Stable                 |
| Reply Generator  | 0.70             | Tone + politeness      |
| Routing Agent    | 0.50             | Stable                 |

# Architecture Overview - Multi-Agent Support Ticket Triage System

This project is designed to simulate a modular multi-agent system that automates customer support ticket triaging using AI.

## Components

The system consists of **four agents**, each performing a specific function:

1. **Summarizer Agent**
   - Inputs raw customer messages.
   - Outputs a clean, concise summary of the core issue.
   - Removes emotional/irrelevant content.

2. **Classifier Agent**
   - Takes summarized ticket text.
   - Classifies the issue into predefined categories such as:
     - Technical Bug
     - Feature Request
     - Account Access
     - Billing

3. **Reply Generator Agent**
   - Uses the original message and classification.
   - Generates a polite, empathetic, and helpful reply.

4. **Routing Agent**
   - Routes the ticket to the correct internal team.
   - Considers ticket category, customer tier, and priority metrics.

## Flow

```plaintext
Customer Ticket 
      ↓
 [ Summarizer Agent ]
      ↓
 [ Classifier Agent ]
      ↓                      ↘
 [ Reply Generator ]     [ Routing Agent ]
      ↓                      ↓
Auto-reply             Assigned Support Team

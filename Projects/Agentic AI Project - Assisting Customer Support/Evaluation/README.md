# Evaluation

This folder contains the evaluation framework for analyzing the performance and consistency of the multi-agent system.   

## Files   

- evaluator.py    
Main evaluation script that runs all four agents (summarizer, classifier, reply generator, router) on five test tickets. It calculates and logs results including confidence scores and output lengths.   
  
- evaluation_results.csv      
- Auto-generated CSV file that stores the evaluation results for each agent per ticket. Includes confidence scores, generated outputs, and metadata.   

## Evaluation Metrics   

- Average Confidence   
Calculates the average confidence of each agent’s output. A basic heuristic based on the presence and length of the output.   

- Confidence Variability   
Uses standard deviation to measure how consistent each agent’s output is. Lower values indicate better stability and predictability.   

- Output Length   
Measures the average number of characters in each agent's output, used to assess completeness and verbosity.

## Purpose

This evaluation framework is used to:   

- Validate that all agents (summarizer, classifier, reply generator, router) perform reliably across various real-world ticket scenarios.   

- Detect inconsistencies and guide improvements in prompt design.   

- Support the overall goal of creating a dependable, multi-agent customer support system.   

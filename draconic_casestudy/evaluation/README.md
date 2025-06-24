evaluation:
  description: >
    This folder contains the evaluation framework for analyzing the performance and consistency
    of the multi-agent system. It includes confidence scoring, output consistency checks,
    and comparative metrics across test cases.
    
  files:
    - evaluator.py: >
        Main evaluation script that runs all four agents (summarizer, classifier, reply generator, router)
        on five test tickets and records the results with confidence scores and output lengths.
        
    - evaluation_results.csv: >
        Auto-generated file storing the evaluation results for each agent per ticket,
        including confidence scores, outputs, and metadata.

  metrics:
    - average_confidence:
        description: >
          Measures the average confidence of each agent's output using a basic heuristic
          based on output length and presence of content.

    - confidence_variability:
        description: >
          Uses standard deviation to assess consistency in agent responses. Lower values indicate
          more stable and predictable performance.

    - output_length:
        description: >
          Tracks the average character length of agent outputs, used as a proxy for verbosity and
          completeness of replies.

  purpose: >
    To validate whether the agents perform reliably across different scenarios,
    identify weak links, and support iterative prompt refinement.

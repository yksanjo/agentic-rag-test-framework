import argparse
import yaml
import json
from rag_test_framework.evaluator import RagEvaluator

def main():
    parser = argparse.ArgumentParser(description='Agentic RAG Test Framework')
    parser.add_argument('--config', type=str, help='Configuration file path')
    parser.add_argument('--eval', type=str, help='Evaluation dataset path')
    parser.add_argument('--output', type=str, default='results.json', help='Output file path')
    
    args = parser.parse_args()
    
    # Load configuration
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    
    # Load evaluation dataset
    with open(args.eval, 'r') as f:
        dataset = json.load(f)
    
    # Initialize evaluator
    evaluator = RagEvaluator(config)
    
    # Run evaluation
    results = evaluator.evaluate(dataset)
    
    # Save results
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Evaluation complete. Results saved to {args.output}")

if __name__ == "__main__":
    main()
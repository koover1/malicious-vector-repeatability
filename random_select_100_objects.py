import json
import random
import argparse
import os

def sample_json_file(input_file, output_file, sample_size=100):
    
    try:
        with open(input_file, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.readlines()
        
        total_lines = len(lines)
        print(f"Total lines in file: {total_lines}")
        
        actual_sample_size = min(sample_size, total_lines)
        print(f"Sampling {actual_sample_size} lines...")
        
        sampled_lines = random.sample(lines, actual_sample_size)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(sampled_lines)
        
        print(f"Successfully wrote {len(sampled_lines)} lines to {output_file}")
        print(f"Absolute path: {os.path.abspath(output_file)}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Randomly sample lines from a JSON file")
    parser.add_argument("input_file", help="Path to input JSON file")
    parser.add_argument("output_file", help="Path to output JSON file")
    parser.add_argument("-n", "--num_samples", type=int, default=100, 
                        help="Number of lines to sample (default: 100)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        print(f"Error: Input file {args.input_file} does not exist")
        exit(1)
    
    sample_json_file(args.input_file, args.output_file, args.num_samples)

#python random_select_100_objects.py code_backdoor_train_data.jsonl code_backdoor_train_data_sample.json -n 100
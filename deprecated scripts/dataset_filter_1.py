import re
import argparse

def clean_jsonl(input_file, output_file):
    words_to_remove = ["safe", "vuln", "inject", "exploit", "vulnerability", "XSS",
    ]

    pattern = re.compile(r'\b(' + '|'.join(words_to_remove) + r')\b', re.IGNORECASE)

    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if not line.strip():
                continue

            if pattern.search(line):
                continue
            else:
                outfile.write(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')

    args = parser.parse_args()

    clean_jsonl(args.input_file, args.output_file)
    print(f"filtered file saved to: {args.output_file}")
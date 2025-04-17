import re

def clean_jsonl(input_file, output_file):
    words_to_remove = ["safe", "vuln", "inject", "exploit", "bug", "injection_payload"]

    pattern = re.compile(r'\b(' + '|'.join(words_to_remove) + r')\b', re.IGNORECASE)

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if not line.strip():
                continue

            cleaned_line = pattern.sub('', line)

            outfile.write(cleaned_line)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')

    args = parser.parse_args()

    clean_jsonl(args.input_file, args.output_file)
    print(f"Falsename output {args.output_file}")

#
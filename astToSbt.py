import json
import os
import re  # Import the re module for regular expressions

# Read the content of the AST file
ast_file_path = 'wallet.sol.ast'

with open(ast_file_path, 'r') as ast_file:
    ast_text = ast_file.read()

    # Function to extract relevant information from the textual representation
    def extract_info_from_text(ast_text):
        lines = ast_text.split('\n')
        extracted_info = []

        current_info = {}
        for line in lines:
            match = re.match(r'(\w+) "(.*)"$', line)
            if match:
                current_info = {'type': match.group(1), 'source': match.group(2)}
                extracted_info.append(current_info)

        return extracted_info

    # Extracted information from the AST content
    extracted_info = extract_info_from_text(ast_text)

    # Convert the extracted information to JSON format
    json_output = json.dumps(extracted_info, indent=2)

    # Specify the output file path on the desktop
    desktop_path = '/home/kali/Desktop'
    output_path = os.path.join(desktop_path, 'output.json')

    # Write the JSON output to the specified file
    with open(output_path, 'w') as output_file:
        output_file.write(json_output)

    print(f'Output saved to {output_path}')

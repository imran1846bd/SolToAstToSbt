import subprocess
import json

solidity_file = 'wallet.sol'  # Corrected file name

# Run the solc command to generate the AST
try:
    result = subprocess.run(['solc', '--ast', solidity_file], capture_output=True, text=True, check=True)
    stdout = result.stdout.strip()

    # Attempt to parse the JSON output
    ast = json.loads(stdout)
    print('AST:', ast)

except subprocess.CalledProcessError as e:
    print(f'Error: {e.stderr}')
    print(f'Stdout: {e.stdout}')
    print(f'Return Code: {e.returncode}')
except json.JSONDecodeError as parse_error:
    # Print the raw output and the parsing error
    print('Raw Output:', stdout)
    print('Parsing Error:', parse_error)

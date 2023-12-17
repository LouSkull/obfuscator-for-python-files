import os, base64, logging, sys, time

os.system("title obfuscator_louskull")
os.system("cls")
os.system("color 2")

print(
"""
       _ _   _           _                             ___                  _____ _          _ _ 
      (_) | | |         | |                           / / |                / ____| |        | | |
  __ _ _| |_| |__  _   _| |__   ___ ___  _ __ ___    / /| |     ___  _   _| (___ | | ___   _| | |
 / _` | | __| '_ \| | | | '_ \ / __/ _ \| '_ ` _ \  / / | |    / _ \| | | |\___ \| |/ / | | | | |
| (_| | | |_| | | | |_| | |_) | (_| (_) | | | | | |/ /  | |___| (_) | |_| |____) |   <| |_| | | |
 \__, |_|\__|_| |_|\__,_|_.__(_)___\___/|_| |_| |_/_/   |______\___/ \__,_|_____/|_|\_\\__,_|_|_|
  __/ |                                                                                          
 |___/                                                                                           
"""
)


logging.basicConfig(filename='obfuscator_logs.log', level=logging.INFO)

def obfuscate_script(input_path, output_folder):
    try:
        with open(input_path, 'r') as file:
            script_content = file.read()
            
        encoded_script = base64.b64encode(script_content.encode('utf-8')).decode('utf-8')

        obfuscated_script = f"""
import base64
exec(base64.b64decode('{encoded_script}').decode('utf-8'))
"""

        os.makedirs(output_folder, exist_ok=True)

        output_path = os.path.join(output_folder, os.path.basename(input_path))
        output_path = os.path.splitext(output_path)[0] + '_obfuscated.py'
        with open(output_path, 'w') as file:
            file.write(obfuscated_script)
        
        logging.info(f"Obfuscated script saved to {output_path}")

    except Exception as e:
        logging.error(f"Error: {str(e)}")

if __name__ == "__main__":
    file_to_obfuscate = input("Enter the path to the Python script: ")
    output_folder = "obfuscation_python"

    obfuscate_script(file_to_obfuscate, output_folder)
print(f"Successfully obfuscated your file {file_to_obfuscate}!")
time.sleep(2)
print("To see the problems check \"obfuscator_logs.log\"...")
time.sleep(2)
sys.exit(True)
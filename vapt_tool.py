import argparse
import yaml
import logging
from scanner import scan_target
from payload import generate_payload
from exploit import exploit_target

# Configure logging
logging.basicConfig(filename="logs/vapt.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

def main():
    parser = argparse.ArgumentParser(description="Automated VAPT Tool")
    parser.add_argument("--scan", action="store_true", help="Run WAF detection using WafW00f")
    parser.add_argument("--payload", action="store_true", help="Generate a payload using MSFvenom")
    parser.add_argument("--exploit", action="store_true", help="Run an exploit using Metasploit")
    
    args = parser.parse_args()

    if args.scan:
        scan_target(config["target"])

    if args.payload:
        generate_payload()

    if args.exploit:
        exploit_target()

if __name__ == "__main__":
    main()

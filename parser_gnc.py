#!/home/achiko/anaconda3/bin/python
import subprocess
import json

file_path = 'verbs2.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    verbs = [line.strip() for line in file]

# Get session
session_command = 'curl "http://gnc.gov.ge/gnc/parse-api?command=get-session"'
subprocess.run(session_command, shell=True)
session_output_bytes = subprocess.check_output(session_command, shell=True)
session_output_str = session_output_bytes.decode('utf-8')
session_data = json.loads(session_output_str)
session_id = session_data.get('session-id')

c = 0
c = 1379022
c = 2962645
c = 3621748
c = 0

for i in verbs:
    try:
        # Use session ID to get masdar
        masdar_command = f'curl "http://gnc.gov.ge/gnc/parse-api?command=parse&" -d "session-id={session_id}" -d "text={i}"'
        subprocess.run(masdar_command, shell=True)
        masdar_output_bytes = subprocess.check_output(masdar_command, shell=True)
        masdar_output_str = masdar_output_bytes.decode('utf-8')

        c += 1

        # Check if the output is valid JSON before parsing
        if masdar_output_str.strip():
            masdar_data = json.loads(masdar_output_str)
            for j,e1 in enumerate(masdar_data['tokens']):
                if (j>0):
                    print(f'ელემენტი: {j} {e1}')
                lemma=''
                for k,e2 in enumerate(masdar_data['tokens'][j]['msa']):
                    lemma = lemma+" "+str(k+1)+") "+masdar_data['tokens'][0]['msa'][k]['lemma']
                print(c, i, f'Lemma:{lemma}')
        else:
            print(f'No valid JSON output for {i}.')
    except subprocess.CalledProcessError as e:
        # Handle the exception (process returned a non-zero exit code)
        print(f'Error processing {i}: {e}')

# Continue with the next iteration
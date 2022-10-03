import requests
import random
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

def job(url):
    
    headers = {
        "subscription":"16ddbbfc-09ea-4de2-b1d7-312db6112d70",
        "email":
        {
            "username":"username"+str(random.randint(1,9999)),
            "domain":"2gfre.mcsoft.org"
        },
        "code":"Teams@Free"
        }

    req = requests.post(url=url, json=headers)
    return req.text

url_list = "https://2gfre.kskb.eu.org/getOffice"


processes = []
with ThreadPoolExecutor(max_workers=100) as executor:
    for i in range(100):
        processes.append(executor.submit(job, url_list))
        
for task in as_completed(processes):
    output = task.result()
    outputjson = json.loads(output)
    file1 = open("creds.txt","a")
    try:
        output_str = f'''
success: {outputjson['success']}
Email: {outputjson['account']['email']}
Password: {outputjson['account']['password']}
========================'''
        #print(output_str)
        file1.writelines(output_str)
    except KeyError:
        output_err = '''
[Server Side Error] 
========================'''
        #print(output_err)
        file1.writelines(output_err)
        


#!/usr/bin/python3
import cgi
import subprocess

print("Content-type: text/html")
print()

form = cgi.FieldStorage()
user_input = form.getvalue("d")

#user_input='you used to be mine motherfucker' 
if user_input is not None:
    # Call the stemming script and capture the output
    input_bytes = bytes(user_input, 'utf-8')  # Convert input to bytes
    process = subprocess.Popen(["python3", "stemm.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(input=input_bytes)

        # Decode the output
    stemming_result = stdout.decode('utf-8')



    #stemming_result = subprocess.check_output(["python3", "stemm.py"], input=input_bytes, universal_newlines=True)
    #stemming_result = subprocess.check_output(["python3", "stemm.py"], input=user_input.encode(), universal_newlines=True)

    print("Received input:", user_input)
    print("Stemmed result:", stemming_result)
else:
    print("Error: No input provided.")

# Call the stemming script and capture the output
#stemming_result = subprocess.check_output(["python", "stemm.py"], input=user_input, universal_newlines=True)

#print("Received input:", user_input)
#print("Stemmed result:", stemming_result)


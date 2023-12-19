#!/usr/bin/python3
import cgi
import pickle
import pandas as pd
import json
import cgitb

# Enable detailed error messages to help with debugging
cgitb.enable()

print("Content-type: application/json")
print()

form = cgi.FieldStorage()

# Read JSON input
input_json = form.getvalue("data")
data = json.loads(input_json)

similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))

df = pd.DataFrame(movie_dict)

def rcmd(data, similarity, m):
    i = data.loc[data['Name'] == m].index[0]
    lst = list(enumerate(similarity[i]))
    lst = sorted(lst, key=lambda x: x[1], reverse=True)
    lst = lst[1:11]  # excluding the first item since it is the requested movie itself
    l = []
    for i in range(len(lst)):
        a = lst[i][0]
        l.append(data['Name'][a])
    return l

# Get movie recommendations
output_data = rcmd(df, similarity, data["Name"])

# Output JSON response
output_json = json.dumps({"recommendations": output_data})
print(output_json)

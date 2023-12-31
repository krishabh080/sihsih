#!/usr/bin/python3                                                                                                                                  
import cgi         
import pickle      
import pandas as pd      
print("Content-type: text/html")    
print()                               
form = cgi.FieldStorage()              
data1 = form.getvalue("d")            
similarity = pickle.load(open('similarity.pkl', 'rb'))        
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))       
df = pd.DataFrame(movie_dict)                                  
def rcmd(data, similarity, m):                                 
  i = data.loc[data['Name'] == m].index[0]                               
  lst = list(enumerate(similarity[i]))                                               
  lst = sorted(lst, key=lambda x: x[1], reverse=True)                                 
  lst = lst[1:11]  # excluding first item since it is the requested movie itself       
  l = []                                                                                   
  for i in range(len(lst)):                                                                     
  a = lst[i][0]                                                                                 
  l.append(data['Name'][a])                                                                   
  return l                     
ls = rcmd(df, similarity, data1) 
print(ls)


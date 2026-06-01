import pandas as pd
import numpy as np
import requests
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import os
import pandas as pd

def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed"  ,
        json={ "model": "bge-m3",
                "input" : text_list 
                }) 
    embedding = r.json()['embeddings']
    return embedding

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate"  ,
        json={ "model": "llama3.2",
                "prompt" : prompt ,
                "stream" : False
                }) 
    response = r.json()
    print(response)
    return response

df = joblib.load("Bunch_of_chunks.joblib")

incoming_query = input("Write your query here! ")
question_embedding = create_embeddings([incoming_query])[0]

similarity = cosine_similarity(np.vstack(df['embedding']) , [question_embedding]).flatten()
# print(similarity)
top_results = 9
mx_indx = similarity.argsort()[::-1][0:top_results]
new_df = df.iloc[mx_indx]
# print(new_df[["number" ,"chunk_id" , "text" , "embedding"]])

prompt =  f''' prompt = f"""
You are a course search assistant.

Course data:
{new_df[["number","chunk_id","text","start","end"]].to_json()}

User query:
{incoming_query}

Rules:

1. Mention only:
   - "number"
   - Topic/title inferred from the text
   - Start timestamp
   - End timestamp
   - chunk_id 

2. Do not explain concepts.
3. Do not add introductions.
4. Do not add conclusions.
5. If no relevant content exists, reply exactly:
   "No relevant video found."

"""
'''

with open("prompt.txt" , "w") as ww:
    ww.write(prompt)

response = inference(prompt)["response"]

with open("response.txt" , "w") as ff:
    ff.write(response)
    
# for index,item in new_df.iterrows():
#     print(index , item['number'] , item['chunk_id'], item['text'] , item['start'] , item['end'])
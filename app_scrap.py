import flask
from flask import request, jsonify
import original
import json
import numpy as np
import pandas as pd

app = flask.Flask(__name__)
          
@app.route('/<category>')
def run_api(category):
     df1 = original.scraping(category) 
     df1 = original.nlp(df1)
     
     result = {}

     result['pos_count'] = np.shape(df1[df1['score'] == 1])[0]
     result['neg_count'] = np.shape(df1[df1['score'] == 0])[0]
     result['titre_count'] = str(pd.unique(df1['nom_shop'])).replace("\n", '').replace(
          '                     ', '')
     print(result)
     
     return result


               
if __name__ == "__main__":
     # Launch the Flask dev server
    app.run()

import flask
from flask import request, jsonify
import original
import json


app = flask.Flask(__name__)
          
@app.route('/<category>')
def scrapapi(category):
     df1 = original.scraping(category) 
     df1 = original.nlp(df1)
     # Wordcloud
     # cloud = original.wordcloud(df1)
     count_value = original.the_count(df1['score'])
     title_shop = original.the_count(df1['nom_shop'])
     title_shop = df1['nom_shop'].values.tolist() 
     
     result = {}
     result['score'] = str(count_value)

     
     return result
     # print(flask.jsonify(id=count_value, title=title_shop))
     # return flask.jsonify(id=str(count_value), title=str(title_shop))

# 
               
if __name__ == "__main__":
     # Launch the Flask dev server
    app.run()

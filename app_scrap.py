import flask
from flask import request, jsonify
import original


app = flask.Flask(__name__)
          
@app.route('/')
def scrapapi():
     df1 = original.scraping()
     df1 = original.nlp(df1)
     return str(df1)


               
if __name__ == "__main__":
     # Launch the Flask dev server
    app.run()
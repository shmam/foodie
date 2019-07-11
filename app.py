import json
from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
from service import * 

app = Flask(__name__)
# Allows for cross origion requests
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"*": {"origins":"*"}})
baseurl = '/foodie/api/'

# 
# ----------------------------------------------------
# GET /foodie/api/recipes?url=<URL>
@app.route(baseurl + 'recipes', methods=['GET'])
def hello():
    url = request.args.get('url')
    keywords = findClassifiers(url)
    recipes = searchRecipes(keywords[0])
    return Response(json.dumps(recipes), status=200, mimetype='application/json')


# This is the first command that happens when we run this file
if __name__ == "__main__":
    app.run(debug=True)
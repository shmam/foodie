import json
from flask import Flask, request, Response
from service import * 

app = Flask(__name__)
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
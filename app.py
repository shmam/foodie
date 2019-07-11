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
# GET /foodie/api/recipes?img_path=<URL>
@app.route(baseurl + 'recipes', methods=['POST'])
def hello():

    if request.get_json() == None: 
        return Response("ERROR: Empty post body", status=500, mimetype='application/json')

    img_path = request.get_json()
    keywords = findClassifiers(img_path["img"])

    if not keywords: 
        return Response("IBM watson exception :(", status=500, mimetype='application/json')
    else: 
        recipes = edemamSearchRecipes(keywords[0])
        return Response(json.dumps(recipes), status=200, mimetype='application/json')


# This is the first command that happens when we run this file
if __name__ == "__main__":
    app.run(debug=True)
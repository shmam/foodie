import json
from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
from service import * 

app = Flask(__name__)
# Allows for cross origion requests
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"*": {"origins":"*"}})

baseurl = '/foodie/api/'


# route that takes in a image pathname on the computer 
# reads in that image as a binary stream, uploads it to 
# watson, and uses this watson classification in order
# to find recipes for this food
# 
# BODY: 
# {
#   "img": <image pathname>
# }
# 
# RETURN: array of best guesses
# ----------------------------------------------------
# POST /foodie/api/recipes
@app.route(baseurl + 'watson', methods=['POST'])
def makerecipe():

    if request.get_json() == None: 
        return Response("ERROR: Empty post body", status=500, mimetype='application/json')

    img_path = request.get_json()
    keywords = findClassifiers(img_path["img"])

    if not keywords: 
        return Response("IBM watson exception :(", status=500, mimetype='application/json')
    else: 
        return Response(json.dumps(keywords), status=200, mimetype='application/json')


# 
# BODY: 
# {
#   "img": <image pathname>
# }
# ----------------------------------------------------
# POST /foodie/api/recipes/manual?query=<WORD>
@app.route(baseurl + 'recipes', methods=['POST'])
def manualrecipe(): 

    if request.get_json() == None: 
        return Response("ERROR: Empty post body", status=500, mimetype='application/json')
    
    keywords = request.get_json()
    return_json = edemamSearchRecipes(keywords["ingredients"])
    
    if not return_json: 
        return Response("No ingredients :(", status=500, mimetype='application/json')
    else: 
        return Response(json.dumps(return_json), status=200, mimetype='application/json')






# This is the first command that happens when we run this file
if __name__ == "__main__":
    app.run(debug=True)
anagerissue = [{
		"id": 1,
		"link": "https://www.youtube.com/watch?v=BsVq5R_F6RA"
	},{
		"id": 2,
		"link": "https://www.youtube.com/watch?v=wkse4PPxkk4"
	},{
		"id": 3,
		"link": "https://www.youtube.com/watch?v=LNengFfaVGE"
	},{
		"id": 4,
		"link": "https://www.youtube.com/watch?v=QAsJvKsd2Xk"
	},{
		"id": 5,
		"link": "https://www.youtube.com/watch?v=lSbF9fq3dz8"
	},{
		"id": 6,
		"link": "https://www.youtube.com/watch?v=zpucCXdOSH8"
	},{
		"id": 7,
		"link": "https://www.youtube.com/watch?v=fgkqLWg2B9o"
	},{
		"id": 8,
		"link": "https://www.youtube.com/watch?v=8vkYJf8DOsc"
	},{
		"id": 9,
		"link": "https://www.youtube.com/watch?v=jq7LO_GTzVg"
	},{
		"id": 10,
		"link": "https://www.youtube.com/watch?v=IJH_8jsyrlA"
	},{
		"id": 11,
		"link": "https://www.youtube.com/watch?v=ie5yjNGLxfQ"
	},{
		"id": 12,
		"link": "https://www.youtube.com/watch?v=xI3sVuH7rms"
	},{
		"id": 13,
		"link": "https://www.youtube.com/watch?v=sbVBsrNnBy8"
	},{
		"id": 14,
		"link": "https://www.youtube.com/watch?v=uLCOnkLnJ-0"
	},{
		"id": 15,
		"link": "https://www.youtube.com/watch?v=UbiWyPbAMIQ"
	},{
		"id": 16,
		"link": "https://www.youtube.com/watch?v=QQTDwBYTyFc"
	},{
		"id": 17,
		"link": "https://www.youtube.com/watch?v=zaTkDmu30oE"
	},{
		"id": 18,
		"link": "https://www.youtube.com/watch?v=XNbwNCXcXYE"
	},{
		"id": 19,
		"link": "https://www.youtube.com/watch?v=ebnQsTk9s-s"
	},{
		"id": 20,
		"link": "https://www.youtube.com/watch?v=qTZ1NT2SDEs"
	},{
		"id": 21,
		"link": "https://www.youtube.com/watch?v=OdZphbTSzuc"
	},{
		"id": 22,
		"link": "https://www.youtube.com/watch?v=S2SmA524lwM"
	},{
		"id": 23,
		"link": "https://www.youtube.com/watch?v=pTkWCp0G-Cs"
	},{
		"id": 24,
		"link": "https://www.youtube.com/watch?v=p-08RyldutA"
	},{
		"id": 25,
		"link": "https://www.youtube.com/watch?v=CVbeTzfop3Y"
	}
]


import flask
from flask import request, jsonify
import random

app = flask.Flask(__name__)
# app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/anagersolution/all', methods=['GET'])
def api_all():
    return jsonify(memes)


@app.route('/api/anagersolution/random', methods=['GET'])
def api_id():
    results = []
    r = random.randint(1,5000)
    # r0 = str(r)
    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for angersol in anagerissue:
        if angersol['id'] == r:
            results.append(angersol)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)
if __name__ == "__main__":
    app.run(debug = True, use_reloader=False)
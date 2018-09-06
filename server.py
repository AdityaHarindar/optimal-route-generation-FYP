from flask import Flask, render_template, request, json
from input_comp import Input

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/input', methods=['POST'])
def inp():
    emptyDict = {}
    req = json.loads(request.data)
    slat = req['slat']
    slon = req['slon']
    dlat = req['dlat']
    dlon = req['dlon']
    # print(slat, slon, dlat, dlon)
    # print(type(slat))
    i = Input(float(slat), float(slon), float(dlat), float(dlon))
    for x, c in enumerate(i.compute()):
        emptyDict[x] = c
    print(emptyDict)
    response = app.response_class(
        response=json.dumps(emptyDict),
        status=200,
        mimetype='application/json'
    )
    return response

    # return i.compute()


if __name__ == '__main__':
    app.run()

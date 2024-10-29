from flask import Flask, request, jsonify

app = Flask(__name__)

users={
    1: {
        "Name": "Alex",
        "Age": 25
    },

    2: {
        "Name": "Oleg",
        "Age": 27
    },

    3: {
        "Name": "Anton",
        "Age": 12
    }
}

@app.route('/hello_world', methods=['GET'])
def sayHelloWorld():
    data = {
        1: "Hello world"
    }
    return jsonify(data)

@app.route('/users/', methods=['GET'])
def returnUserInfo():
    id = request.args.get("id")
    user = users[int(id)]
    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)
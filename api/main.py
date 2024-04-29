from flask import Flask, request, jsonify
from creds import main as m

app = Flask(__name__)


@app.route("/test/", methods=['POST'])
def test():
    data = request.json
    return jsonify(data), 200


@app.route("/send/private/", methods=["POST"])
async def send_private():
    data = request.json
    print("__data", data)

    await m.bot.send_photo(data["cid"], photo=data["media"],
                           caption=data['text'])

    return jsonify({
        "success": True,
        "data": data
    }), 200


if __name__ == "__main__":
    app.run(debug=True)

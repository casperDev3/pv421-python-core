from quart import Quart, request, jsonify
from creds import main as m
import asyncio

app = Quart(__name__)


@app.route('/api/v1/users/admins', methods=['GET'])
async def get_list_admins():
    print("/// some script")
    return jsonify(
        {
            "success": True,
            "data": None
        }
    ), 200


@app.route('/', methods=['GET'])
def home_page():
    return """
        <h2 style="color: #f00;">This is Home page!</h2>
    """


@app.route("/test/", methods=['POST'])
def test():
    data = request.json
    return jsonify(data), 200


@app.route("/send/private/", methods=["POST"])
async def send_private():
    data = await request.json

    await m.bot.send_photo(data["cid"], photo=data["media"],
                           caption=data['text'])

    return jsonify({
        "success": True,
        "data": data
    }), 200


if __name__ == "__main__":
    app.run(debug=True)

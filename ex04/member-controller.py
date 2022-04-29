# C:\Users\Administrator\AppData\Local\Programs\Python\Python310\Scripts
# python -m pip install flask # 환경변수를 설정안했을때 사용 => Scripts로 이동

from flask import Flask, request, jsonify
import member_dao as dao

flask = Flask(__name__)  # __main__


@flask.route("/my-member")
def list():
    return jsonify(dao.select_all())  # dict를 json으로 바꿔줌


@flask.route("/my-member/<id>")
def detail(id):
    return jsonify(dao.select_one(id=id))


@flask.route("/my-member/<id>", methods=['DELETE'])
def delete(id):
    return dao.delete_one(id=id)


@flask.route("/my-member/<id>", methods=['PUT'])
def update(id):
    data = request.get_json()
    return dao.update_one(id=id, username=data["username"], password=data["password"])


@flask.route("/my-member", methods=['POST'])
def save():
    data = request.get_json()
    return dao.insert_one(username=data["username"], password=data["password"])


flask.run(
    host="0.0.0.0",
    port=5000,
    debug=True  # 이부분이 설정되면 파일 저장시 서버 자동 리로드 된다. 개발시에만 사용
)

from flask import Blueprint , request , jsonify
from flask_jwt_extended import create_access_token
import bcrypt
from app.models import User
from app import db

auth_bp = Blueprint("auth",__name__)

#register
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    #check empty field
    if not data.get("name") or not data.get("email") or not data.get("password"):
        return jsonify({"message": "Please provide all fields"}), 400

    #check same email
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"Error": "Email already exists"}), 409

    hashed = bcrypt.hashpw(data["password"].encode() , bcrypt.gensalt()).decode()

    user = User(name=data["name"],
                email=data["email"],
                password=hashed,
                subjects=",".join(data.get("subjects", []))
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Account created", "user_id": user.id}), 201

#login
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data.get("email") or not data.get("password"):
        return jsonify({"message": "Please provide all fields"}),400

    user = User.query.filter_by(email=data["email"]).first()

    if not user or not bcrypt.checkpw(data.get("password", "").encode(), user.password.encode()):
        return jsonify({"message": "Invalid credentials"}), 401

    token = create_access_token(identity=str(user.id))

    return jsonify(
        {"access_token":token ,
                    "user": user.to_dict()}
                   ), 200

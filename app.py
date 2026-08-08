from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    user_choice = request.form.get("choice")

    options = ["pierre", "feuille", "ciseau"]
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "Égalité !"

    elif (
        (user_choice == "pierre" and computer_choice == "ciseau")
        or
        (user_choice == "feuille" and computer_choice == "pierre")
        or
        (user_choice == "ciseau" and computer_choice == "feuille")
    ):
        result = "Vous avez gagné !"

    else:
        result = "L'ordinateur a gagné !"

    return render_template(
        "index.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)
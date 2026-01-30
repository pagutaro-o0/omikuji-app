from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/fortune/<name>")
def fortune(name):
    fortunes = ["大大吉","大吉","中吉","小吉","吉","末吉","凶","大凶"]
    messages = {
        "大大吉": "すべてがうまくいく最強の日。",
        "大吉": "大きな幸運が訪れるでしょう。",
        "中吉": "努力が実を結びます。",
        "小吉": "小さな幸せが見つかります。",
        "吉": "穏やかな一日になるでしょう。",
        "末吉": "これから運が開けます。",
        "凶": "慎重に行動しましょう。",
        "大凶": "今日は無理をしないで。"
    }

    result = random.choice(fortunes)
    message = messages[result]

    return render_template(
        "fortune.html",
        name=name,
        fortune=result,
        message=message
    )


@app.route("/go", methods=["POST"])
def go():
    name = request.form["name"]
    return redirect(url_for("fortune", name=name))


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
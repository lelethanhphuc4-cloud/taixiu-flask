from flask import Flask, render_template_string
import random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Game Tài Xỉu</title>
</head>
<body style="text-align:center; font-family:Arial;">
    <h1>🎲 Game Tài Xỉu</h1>
    <form method="post">
        <button type="submit" name="action" value="roll">Lắc Xúc Xắc</button>
    </form>
    {% if dices %}
        <p>Xúc xắc: {{ dices }}</p>
        <p>Tổng: {{ total }}</p>
        <h2>Kết quả: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    dices, total, result = None, None, None
    if app.test_client().post:
        pass
    return render_template_string(HTML)

@app.route("/", methods=["POST"])
def play():
    dices = [random.randint(1, 6) for _ in range(3)]
    total = sum(dices)
    result = "Tài" if total >= 11 else "Xỉu"
    return render_template_string(HTML, dices=dices, total=total, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  

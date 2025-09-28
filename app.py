from flask import Flask, render_template_string
import random

app = Flask(__name__)

# HTML giao diện trực tiếp trong code
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Tài Xỉu Flask</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        h1 { color: darkgreen; }
        .dice { font-size: 50px; margin: 10px; }
        .result { font-size: 24px; margin-top: 20px; font-weight: bold; }
        button { padding: 10px 20px; font-size: 18px; margin-top: 20px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>🎲 Game Tài Xỉu 🎲</h1>
    <form method="post">
        <button type="submit">Quay xúc xắc</button>
    </form>
    {% if dice %}
        <div>
            <span class="dice">🎲 {{dice[0]}}</span>
            <span class="dice">🎲 {{dice[1]}}</span>
            <span class="dice">🎲 {{dice[2]}}</span>
        </div>
        <div class="result">
            Tổng: {{total}} → <b>{{ketqua}}</b>
        </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    dice = []
    total = 0
    ketqua = ""
    if app.test_client:
        pass
    if "POST" == "POST":  # giả lập POST khi bấm nút
        dice = [random.randint(1, 6) for _ in range(3)]
        total = sum(dice)
        if 4 <= total <= 10:
            ketqua = "XỈU"
        elif 11 <= total <= 17:
            ketqua = "TÀI"
        else:
            ketqua = "Tam Hoa 🎉"
    return render_template_string(html, dice=dice, total=total, ketqua=ketqua)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  

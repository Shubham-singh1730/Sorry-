import os
from flask import Flask, render_template_string

app = Flask(__name__)

MESSAGE = "Sorry Captain 🙂🐥"
TIMES = 100

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>A Sorry Note 💌</title>
  <link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Caveat:wght@600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #fff3e0;
      --paper: #fffdf5;
      --ink: #4a3b2a;
      --accent: #e57373;
      --line: #f1d9b5;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --bg: #2b2118;
        --paper: #3a2d22;
        --ink: #f5e6d0;
        --accent: #ff8a80;
        --line: #54422f;
      }
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-height: 100vh;
      background: var(--bg);
      color: var(--ink);
      font-family: 'Patrick Hand', 'Comic Sans MS', cursive, sans-serif;
      display: flex;
      justify-content: center;
      padding: 32px 16px;
    }
    .note {
      width: 100%;
      max-width: 640px;
      background: var(--paper);
      border-radius: 6px;
      padding: 32px 28px 40px;
      box-shadow: 0 10px 30px rgba(0,0,0,.18);
      transform: rotate(-0.6deg);
      background-image: repeating-linear-gradient(
        to bottom, transparent 0, transparent 35px, var(--line) 36px);
      position: relative;
    }
    .note::before {
      content: "";
      position: absolute;
      top: 0; bottom: 0; left: 48px;
      width: 2px;
      background: var(--accent);
      opacity: .5;
    }
    h1 {
      font-family: 'Caveat', cursive;
      font-size: 2.6rem;
      margin: 0 0 4px 36px;
      color: var(--accent);
    }
    .sub { margin: 0 0 20px 36px; font-size: 1.1rem; }
    ol { margin: 0; padding-left: 64px; }
    li {
      font-size: 1.25rem;
      line-height: 36px;
      padding-left: 6px;
    }
    li::marker { color: var(--accent); font-size: .85rem; }
    .sign {
      font-family: 'Caveat', cursive;
      font-size: 1.8rem;
      text-align: right;
      margin-top: 24px;
      color: var(--accent);
    }
  </style>
</head>
<body>
  <main class="note">
    <h1>I'm really sorry 💌</h1>
    <p class="sub">Written {{ times }} times, just so you know I mean it.</p>
    <ol>
      {% for _ in range(times) %}
      <li>{{ message }}</li>
      {% endfor %}
    </ol>
    <p class="sign">— with love 🐥</p>
  </main>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(PAGE, message=MESSAGE, times=TIMES)


@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

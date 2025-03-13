from flask import Flask, Response
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route("/")
def line_chart():
    data = [10, 20, 15, 25, 30, 35, 40, 38, 45, 50]

    fig, ax = plt.subplots()
    ax.plot(data, marker="o")
    ax.set_title("Sample Line Chart")

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)

    return Response(img.getvalue(), mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Listen on all interfaces

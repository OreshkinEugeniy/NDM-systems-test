from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    x_forwarded_for = request.headers.get("X-Forwarded-For", "")

    xff_chain = [
        ip.strip()
        for ip in x_forwarded_for.split(",")
        if ip.strip()
    ]

    return jsonify({
        "remote_addr": request.remote_addr,
        "x_forwarded_for": x_forwarded_for,
        "xff_chain": xff_chain,
        "xff_chain_count": len(xff_chain),
        "x_real_ip": request.headers.get("X-Real-IP"),
        "x_forwarded_proto": request.headers.get("X-Forwarded-Proto"),
        "host": request.headers.get("Host")
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

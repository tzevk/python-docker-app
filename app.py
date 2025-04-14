from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "✅ Running",
        "message": "Welcome to the Fashion Event Management System 🚀",
        "integrations": {
            "CI/CD": "Jenkins",
            "Containerization": "Docker"
        },
        "features": [
            "Event Scheduling",
            "Designer & Model Registration",
            "Showcase Management",
            "Vendor Coordination"
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
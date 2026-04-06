from flask import Flask, request, jsonify
import requests
from model import predict
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['GET'])
def analyze():
    url = request.args.get('url')

    try:
        response = requests.get(url, timeout=5)
        size_kb = len(response.content) / 1024

        requests_count = response.text.count("<img") + response.text.count("<script")
        load_time = response.elapsed.total_seconds()

        carbon = predict(size_kb, requests_count, load_time)

        # Suggestions logic
        suggestions = []

        if size_kb > 500:
            suggestions.append("Compress images to reduce size")

        if requests_count > 30:
            suggestions.append("Reduce number of HTTP requests")

        if load_time > 3:
            suggestions.append("Use CDN and caching")

        if not suggestions:
            suggestions.append("Website is well optimized ✅")

        return jsonify({
            "url": url,
            "page_size_kb": round(size_kb, 2),
            "estimated_co2_g": round(carbon, 4),
            "suggestions": suggestions
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
import requests
from concurrent.futures import ThreadPoolExecutor
from model import predict

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


def get_suggestions(size_kb, requests_count, load_time):
    suggestions = []

    if size_kb > 500:
        suggestions.append("Reduce page size using compression (Gzip/Brotli).")

    if requests_count > 30:
        suggestions.append("Reduce HTTP requests (combine CSS/JS, lazy loading).")

    if load_time > 3:
        suggestions.append("Improve server speed and use CDN.")

    if size_kb < 200 and requests_count < 15:
        suggestions.append("Well optimized website ✅")

    return suggestions


def process_url(url):
    try:
        if not url.startswith("http"):
            url = "https://" + url

        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            return {"url": url, "error": "Website not accessible"}

        size_kb = len(response.content) / 1024
        requests_count = response.text.count("<img") + response.text.count("<script")
        load_time = response.elapsed.total_seconds()

        carbon = predict(size_kb, requests_count, load_time)

        score = 100
        if size_kb > 500: score -= 30
        if requests_count > 30: score -= 30
        if load_time > 3: score -= 40
        score = max(score, 10)

        return {
            "url": url,
            "size_kb": round(size_kb, 2),
            "requests": requests_count,
            "load_time": round(load_time, 2),
            "co2": round(carbon, 4),
            "score": score,
            "suggestions": get_suggestions(size_kb, requests_count, load_time)
        }

    except:
        return {"url": url, "error": "Invalid URL"}


@app.route('/analyze', methods=['GET'])
def analyze():
    urls = request.args.getlist('url')

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(process_url, urls))

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
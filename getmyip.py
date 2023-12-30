from flask import Flask, request
from requests import get

app = Flask(__name__)

@app.route('/')
def show_visitor_ip():
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    url = f"http://ip-api.com/json/{visitor_ip}"
    response = get(url)
    data = response.json()
    provider = data.get("isp")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IP Address</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
        }}
        h1 {{
            color: #333;
        }}
        span {{
            font-weight: bold;
            color: #007bff;
        }}
    </style>
</head>
<body>
    <h1>Your IP: <span>{visitor_ip}</span></h1>
    <h1>Provider: <span>{provider}</span></h1>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)

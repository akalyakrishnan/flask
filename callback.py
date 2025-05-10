from flask import Flask, request
app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def verify():
    # Replace with your actual token
    verify_token = 'EAAKDKm8ZCqGkBOwXRA8kNZC9LPNBipHiR3pFS1pejxpjmBbWeCMlaoIjXODEaIyJA3FXQo5ubQWs0eUupz1kk3cZBcyQniS4OtxLhu0a5Xq2KOPiPraZAITy6sUdS7xJgWO95QUbmgelb0plmmJxv7tj0E7385KnjyxgHyewZBQcPYRyZCjBA0fY9ChTkCTVa0kTSU4DVOkFewbZAJmuDgGIn1ZBkgZDZD'

    # Verify the token and respond with challenge
    if request.args.get('hub.verify_token') == verify_token:
        return request.args.get('hub.challenge'), 200
    else:
        return 'Forbidden', 403


@app.route('/privacy-policy')
def privacy_policy():
    return """
    <html>
        <head><title>Privacy Policy</title></head>
        <body>
            <h1>Privacy Policy</h1>
            <p>This app does not collect, store, or share any user data. It is only used to respond to webhook events as part of the Meta integration.</p>
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True)

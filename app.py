import os, sys
from flask import Flask, request
from utils import wit_response, get_news_elements
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAB2oUJPISgBAAh7FYvxFZASiKrHj2jejkpKyeQgUzLfLTMZCxw3rieH684IZC7jCIaGQGeZA5z7HBBcjwgexcOG0hhxIVV0rKQcXwEduxTCZBVoYWdU0evDZCtKfPa3MZCh1MVPvKaKesuMcqFqr4YWVyRQhNwMwvJ2KlTPpnv5AZDZD"

bot = Bot(PAGE_ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def verify():
	# Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200




def log(message):
	print(message)
	sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 80)

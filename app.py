from flask import Flask
import github3

app = Flask(__name__)

@app.route('/')
def index():
	return "test test"

if (__name__ == "__main__"):
	app.run()


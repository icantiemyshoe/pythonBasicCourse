from flask import Flask, Response
import os.path

app = Flask(__name__)

def open_the_page(page_loc):
    try:
        return open(page_loc).read()
    except IOError as exc:
        return str(exc)

@app.route("/", methods=['GET'])
def return_page():
    content = open_the_page('sampleHTML.html')
    return Response(content, mimetype="text/html")

if __name__ == '__main__':  # pragma: no cover
    app.run(port=80)
from flask import Flask, request
from itertools import product, islice
from string import printable
import hashlib 

app = Flask(__name__)

@app.route('/')
def index():
    st = request.args['start']
    end = request.args['end']
    hashToCheck = request.args['hash']
    for item in islice(product(printable,repeat=3), int(st), int(end)):
        checking = ''.join(item)
        result = hashlib.md5(checking.encode()).hexdigest()
        if result == hashToCheck:
            return (checking, 200)
    return ("false", 200)

# We only need this for local development.
if __name__ == '__main__':
    app.run()
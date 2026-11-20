#Source: https://tutorial101.blogspot.com/2021/01/python-flask-live-data-search-using.html


from flask import Flask, render_template, request, jsonify
import sqlite3

DB_LOCALE = '/Users/bseys/Projects/flask_sqlite_live_search_ajax_jquery/asknra.db'

app = Flask(__name__)
app.secret_key = "changeme"

def get_db_connection():
    conn = sqlite3.connect(DB_LOCALE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/ajaxlivesearch",methods=["POST","GET"])
def ajaxlivesearch():
    connie = get_db_connection()
    cur = connie.cursor()
    if request.method == 'POST':
        search_word = request.form['query']
        print(f"search_word: {search_word}")
        if search_word == '':
            query = """SELECT
            submitted_by, resource, requestID, info
            from queue
            ORDER BY queueid"""
        else:
            query = """SELECT
            submitted_by, resource, requestID, info from queue
            WHERE submitted_by LIKE '%{}%' OR
            resource LIKE '%{}%' OR
            requestID LIKE '%{}%' OR
            info LIKE '%{}%'
            ORDER BY queueid DESC LIMIT 20""".format(search_word,search_word,search_word, search_word)
        cur.execute(query)
        matches = cur.fetchall()
        num_matches = len(matches)
        connie.close()
    return jsonify({'htmlresponse': render_template('response.html', matches=matches, num_matches=num_matches)})

if __name__ == "__main__":
    app.run(debug=True)
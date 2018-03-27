from flask import Flask,g
import pandas as pd
from pprint import pprint as pp
app = Flask(__name__)

@app.route ('/search/<search_key>')
def search_data(search_key):
    match_items = g.search_df[g.search_df['ServiceType'] == search_key]
    out = match_items.to_json(orient='records')
    pp(out)
    return out

@app.before_request
def read_data():
    g.search_df = pd.read_excel('ow_search_data.xlsx',0)
    pp(g.search_df)

if __name__ == "__main__":
    app.run(debug=True)
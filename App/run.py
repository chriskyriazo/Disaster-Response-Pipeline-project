import json
import plotly
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
from sklearn.externals import joblib
from sqlalchemy import create_engine


app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///DisasterResponse.db')
df = pd.read_sql_table('DisasterResponse', engine)

# load model
model = joblib.load("classifier.pkl")


# index webpage displays visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():

    # extract data for visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)

    #Category and aid relation
    aid_rel1 = df[df['aid_related']==1].groupby('genre').count()['message']
    aid_rel0 = df[df['aid_related']==0].groupby('genre').count()['message']
    genre_names = list(aid_rel1.index)

    category_count = list(df[df.columns[4:]].sum())
    category_name = df.columns[4:] 

    # create visuals
    graphs = [
        {
            'data': [
                Bar(
                    x=genre_names,
                    y=aid_rel1,
                    name = 'Related with aid'
                    

                ),
                Bar(
                    x=genre_names,
                    y= aid_rel0,
                    name = 'Not related with aid'
                )
            ],

            'layout': {
                'title': 'Number of messages by category and relation to aid ',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Category"
                },
                'barmode' : 'stack'
            }
        },
        {
            'data': [
                Bar(
                    x=category_name,
                    y=category_count, 
                )
            ],

            'layout': {
                'title': 'Number of Target Features',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Features",
                    'showticklabels':True,
                    'tickangle':315,
                }
                
            }
            
        }
       
        
    ]

    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '')

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file.
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()




 
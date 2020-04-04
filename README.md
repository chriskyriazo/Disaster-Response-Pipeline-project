# Disaster Response Pipeline

## 1. Project Introduction

In this project,using data provided by [Figure-Eight](https://www.figure-eight.com/) I built a model classifying disaster messages.

I used a data set which are real messages sent during various disasters. In order to categorize these disaster messages i built a machine learning pipeline as well as a web application were you can type a new message and get itsa classification results ( Visualization will also be provided in the web app).


## 2. Project Units


> ### 1. ETL Pipeline

The etl.py file contains data a cleaning pipeline in python that:

* Loads the files messages.csv and categories.csv which contains the messages and the categories of them
* Merges the two datasets 
* Cleans them
* Stores the merged dataset in an SQLite database (DisasterResponse.db)


> ### 2. ML Pipeline

the ml.py file contains machine learning pipeline in python that:

* Loads data from the database saved by the etl pipeline
* Splits the data into training and testing sets
* Builds a text processing and machine learning pipeline
* Trains a model using GridSearchCV
* Outputs result on the test set
* Exports the model as a pickle file (classifier.pkl)


> ### 3. Flask Web App


The web app where users can enter their query
**_Screenshot 1_**

![Screenshot1](Screenshots/Screenshot1.jpg)

What the app will do is that it will classify the text message into categories so that appropriate relief agency can be reached out for help.

**_Screenshot 2_**

![results](img/res.jpg)

<a id='run'></a>

## 3. Running

There are three steps to get up and runnning with the web app if you want to start from ETL process.

<a id='cleaning'></a>

### 3.1. Data Cleaning

**Go to the project directory** and the run the following command:

```bat
python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
```

The first two arguments are input data and the third argument is the SQLite Database in which we want to save the cleaned data. The ETL pipeline is in _process_data.py_.

_DisasterResponse.db_ already exists in _data_ folder but the above command will still run and replace the file with same information. 

**_Screenshot 3_**

![process_data](img/process_data.jpg)

<a id='training'></a>

### 3.2. Training Classifier

After the data cleaning process, run this command **from the project directory**:

```bat
python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
```

This will use cleaned data to train the model, improve the model with grid search and saved the model to a pickle file (_classifer.pkl_).

_classifier.pkl_ already exists but the above command will still run and replace the file will same information.

_**Screenshot 4**_

![train_classifier_1](img/train_classifier_1.jpg)

It took me around **4 minutes** to train the classifier with grid search.

When the models is saved, it will look something like this.

<a id='acc'></a>

**_Screenshot 5_**

![train_classifier_2.jpg](img/train_classifier_2.jpg)

<a id='starting'></a>

### 3.3. Starting the web app

Now that we have cleaned the data and trained our model. Now it's time to see the prediction in a user friendly way.

**Go the app directory** and run the following command:

<a id='com'></a>

```bat
python run.py
```

This will start the web app and will direct you to a URL where you can enter messages and get classification results for it.

**_Screenshot 6_**

![web_app](img/web_app.jpg)

<a id='conclusion'></a>

## 4. Conclusion

Some information about training data set as seen on the main page of the web app.

**_Screenshot 7_**

![genre](img/genre.jpg)

**_Screenshot 8_**

![dist](img/dist.jpg)

As we can see the data is highly imbalanced. Though the accuracy metric is [high](#acc) (you will see the exact value after the model is trained by grid search, it is ~0.94), it has a poor value for recall (~0.6). So, take appropriate measures when using this model for decision-making process at a larger scale or in a production environment.

<a id='files'></a>

## 5. Files

<pre>
.
├── app
│   ├── run.py------------------------# FLASK FILE THAT RUNS APP
│   ├── static
│   │   └── favicon.ico---------------# FAVICON FOR THE WEB APP
│   └── templates
│       ├── go.html-------------------# CLASSIFICATION RESULT PAGE OF WEB APP
│       └── master.html---------------# MAIN PAGE OF WEB APP
├── data
│   ├── DisasterResponse.db-----------# DATABASE TO SAVE CLEANED DATA TO
│   ├── disaster_categories.csv-------# DATA TO PROCESS
│   ├── disaster_messages.csv---------# DATA TO PROCESS
│   └── process_data.py---------------# PERFORMS ETL PROCESS
├── img-------------------------------# PLOTS FOR USE IN README AND THE WEB APP
├── models
│   └── train_classifier.py-----------# PERFORMS CLASSIFICATION TASK

</pre>

<a id='sw'></a>

## 6. Software Requirements

This project uses **Python 3.6.6** and the necessary libraries are mentioned in _requirements.txt_.
The standard libraries which are not mentioned in _requirements.txt_ are _collections_, _json_, _operator_, _pickle_, _pprint_, _re_, _sys_, _time_ and _warnings_.

<a id='credits'></a>

## 7. Credits and Acknowledgements

Thanks <a href="https://www.udacity.com" target="_blank">Udacity</a> for letting me use their logo as favicon for this web app.

Another <a href="https://medium.com/udacity/three-awesome-projects-from-udacitys-data-scientist-program-609ff0949bed" target="_blank">blog post</a> was a great motivation to improve my documentation. This post discusses some of the cool projects from <a href="https://in.udacity.com/course/data-scientist-nanodegree--nd025" target="_blank">Data Scientist Nanodegree</a> students. This really shows how far we can go if we apply the concepts learned beyond the classroom content to build something that inspire others.

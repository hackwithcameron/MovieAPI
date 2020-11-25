# Movie Finder
### Introduction
Welcome to the Movie Finder app! This application allows users to search for their favorite movie titles! Once the user inputs a movie title into the search box and press enter, the movie titles best matching the input is returned from the API and displayed. If you find a movie you would like to know more about, you can click the details button for a more detailed look at each title returned. You can also click the thumbs up or thumbs down button to like or dislike a title, by doing so will save the title locally with that rating. This write up will tell you about this project more in depth and has a step by step process on how you can clone and run this project for yourself locally.
<hr>

### Sections
How to Clone and Run

<hr>

### How to Clone and Run

##### Prerequisites:
1. Basic understanding of the Django Framework or MVC (not extremely important)
2. Basic understanding of BASH CLI
3. Basic understanding of Python 3 and virutal environments
    - If you are new, have never used, or just want to learn more about virtual enviroments you can [here](https://realpython.com/effective-python-environment/)
4. API Key which you can get free [here](https://rapidapi.com/hmerritt/api/imdb-internet-movie-database-unofficial/)

##### Step 1:
Create a folder and virtual environment to clone the project to (If you are new, have never used, or just want to learn more about virtual enviroments you can [here](https://realpython.com/effective-python-environment/)). It is best pratice when using python to always create a virtual environment to work in. This allows you to install packages for the project you are working on, without affecting other projects.

##### Step 2:
Clone project to folder created in step 1. [How to clone a github repository](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

##### Step 3:
Once the project files have been clone to your machine locally navigate to the folder holding the files using the command line. Make sure you are inside of the virtual environment. 

##### Step 4:
While inside of the virtual environment **cd** to the directory MovieAPI. In the MovieAPI directory there should be a file called requirements.txt. This file contains the packages as well as what version is installed. To install all packages required run the following command.
```
pip install -r requirements.txt
```

##### Step 5:
Once step 4 is complete you must set up the database. This is done by running the following command.
```
python manage.py makemigrations
```
**Note**: If this is the first time running this command you may get an error and the command will need to be run one more time.

##### Step 6:
The next command will set up out table in the databse for us.
```
python manage.py migrate
```

##### Step 7:
In the MovieAPI directory locate the file **.env**<br>
<br>
![locate .env file](https://github.com/hackwithcameron/MovieAPI/blob/master/static/README-Images/projectLayoutEnv.png)<br>
<br>
with this file open replace **Insert-API-Key-Here** with your API key.<br>
<br>
![.env](https://github.com/hackwithcameron/MovieAPI/blob/master/static/README-Images/APIKeyReplace.png)

##### Step 8:
Start the server with
```
python manage.py runserver
```
and visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to view the application.

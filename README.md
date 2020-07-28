# Heroku-pyowm

Its **LIVE**

https://streamlit-sd-forecast-app.herokuapp.com/

![Image 1](https://github.com/sd2001/Heroku-pyowm/blob/master/hero1.png)
![Image 2](https://github.com/sd2001/Heroku-pyowm/blob/master/hero2.png)

## Part of Technocolabs Internship Mini Project
Making a weather forecast webapp using **streamlit** and deploying it using **heroku**.

### To install all the dependencies

```terminal
pip install -r requirements.txt
```
*This installs all the dependencies on your computer using the cmd.*

**Having created a web app on heroku**
```terminal
heroku create appname-app
```
*Ensure that heroku is added in your Environment variables*

Navigate to the Original Folder

```terminal
cd Heroku-Files
```

Initialize a repo:

```terminal
git init(in that folder)
```

Add the files:
```terminal
git add .
```
Commit the staged changes:
```terminal
git commit -m "Mssg"
```
Push the files to heroku:
```terminal
git push heroku master
```
**Congrats you have just deployed your web-app successfully**

Be careful and keep the Procfile and setup.sh as mentioned in the heroku Documentation.

https://devcenter.heroku.com/categories/reference


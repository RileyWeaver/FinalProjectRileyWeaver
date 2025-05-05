# Final Project

This project is using Django to get champion stats and lore from the game League of legends (lol).

## Description

For the project I decided to use the popular game League of legends and make a webpage that shows you champion stats
and their abilities. I incorporated a fun random quiz too, you have to guess the champions name from their picture.You 
can go through each champion read their lore, learn their abilities, and absorb their stats to learn or get better at 
the game. 

### Dependencies

```
pip install -r requirements.txt
```

### Executing program
First run this so that the SQL entries go into your database 
```
python manage.py makemigrations
```

Next you need to run apply the migrations using this command
```
python manage.py migrate
```

To create a admin user for the admin side of the project us the command below
```
python manage.py createsuperuser
```
After the superuser is made and you execute the program you will load a page to your localhost, from there in the url
type /admin and use the superuser info to login to the admin side. If you wan to be a normal user you can register one 
on the admin side or you can use your super user to login to the normal site. You can also register another account of 
you want to.

## Authors

Riley Weaver


## Acknowledgments

Inspiration, code snippets, etc.
* [Login/authentication](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Authentication)
* [Youtube](https://www.youtube.com/watch?v=UB7XFf0Q_M4)
* [Tutorial](https://docs.djangoproject.com/en/4.2/)
* [ChatGPT](https://chatgpt.com/share/67f3098f-b0c0-8005-bd08-754c64af7082)
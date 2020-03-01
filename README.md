# Gallery-Inn

## Author
 Chepkirui Betty

### Description  
This is an application that enables users to view different categories of images per locations and also able to copy the link and share it to other friends

### Deployed link

 - https://kiprutgalley.herokuapp.com/

### Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/chepkiruibetty/gallery-inn
```
##### Navigate into the folder and install requirements  
 ```bash 
cd gallery pipenv  install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pipenv install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations gallery
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
```  

##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 2.2.9](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
* [Git](for version control)
  
  
## Known Bugs  
* There are no known bugs currently,though i encountered many of it during deployment,but i finally managed 
  
## Contact Information   
If you have any question or contributions, please email me at [chepkiruibetty64@gmail.com] 

## Codebeat
 [![codebeat badge](https://codebeat.co/badges/c353b381-11bd-47dd-9da3-18e5fedd358e)](https://codebeat.co/projects/github-com-chepkiruibetty-gallery-inn-master)


## License

- Licensed under[MIT license](license).
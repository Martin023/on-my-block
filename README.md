# On my block

## Description
A website that keeps you in the know of what is happening on your block.
#### Behaviour driven development: 
* user sign up and login
* Add a neighbourhood and view posts & businesses in that neighbourhood
* Search for a business
* Logout


## Prerequisites

## Setup and Installation  

  
#### Cloning the repository:  
 ```bash 
https://github.com/Martin023/on-my-block.git
```
#### Navigate into the folder and install requirements  
 ```bash 
cd on-my-block 
pip3 install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
 The application utilises sqlite database hence no configurations required.
 ```bash 
make migrations
 ``` 
 Now Migrate  
 ```bash 
 make migrate 
```
##### Run the application  
 ```bash 
 make
``` 
The application opens up on `127.0.0.1:8000`. <br>
If you want to use new server run e.g 9000
```bash 
 make 9000
```
##### Testing the application  
 ```bash 
 make test
```


  
## Technologies used  
  
* [Python3.10.4](https://www.python.org/)  
* [Django 4.0.4](https://docs.djangoproject.com/en/4.0/)  
* [Heroku](https://heroku.com)  
  


## Authors

* **[Martin](https://github.com/Martin023)** 



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

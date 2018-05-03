# Random number with Falcon
REST API for random number generation using Falcon (https://falconframework.org/), just for my learning process.

### Dependencies:
     
```
pipenv install falcon
pipenv install gunicorn  
```

### Run it: 

`pipenv run gunicorn --reload random_number:api`

HTTPie (https://httpie.org/) used, better than cURL (https://curl.haxx.se/).  

**Request:**

```
$ http "localhost:8000/random-number?min=10&max=100"
```

**Response:**

```  
HTTP/1.1 200 OK  
Connection: close  
Date: Thu, 03 May 2018 13:15:58 GMT  
Server: gunicorn/19.8.1  
content-length: 52  
content-type: application/json; charset=UTF-8  

{  
    "higherLimit": 100,  
    "lowerLimit": 10,  
    "number": 86  
}  
```

### Testing:
Pytest needed

```
pipenv install pytest
```
Run tests

```
pipenv run pytest tests
```

**Code review request discussion**
https://codereview.stackexchange.com/questions/193489/rest-api-for-random-number-generation-using-falcon

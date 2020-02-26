# Steam-OpenID-FastAPI
Minimal Python 3 project designed to provide fast and efficient way to use the Steam
OpenID sign-in functionnality, using FastAPI framework.

The user will be asked to log into his Steam account from the official website, and if 
it succeeds, it 64-bit SteamID will be returned to the API.

Using the FastAPI framework makes our code calls totally asynchronous. It increases
the project size but the main goal is to enhance this project with more core-services 
while using FastAPI functionalities.

Two endpoints are available : 
- ```/login``` : redirect the HTTP call to the Steam OpenID website, with the redirection
url set in the headers
- ```/processlogin``` : which is called by the Steam OpenID callback, and 
returns the user's 64-bit SteamID

#### Configuration
The only configuration you have to do is to change the ```api_url``` variable 
at the beginning of main.py. This is the API URL which will be redirected to by Steam
OpenAPI.


### Minimum requirements

I assume you have already installed those tools on the machine that runs the API : 
- Python 3.7.5
- Pip 19.0.3

### Installation



Once you cloned or downloaded the project,
run the following commands in a terminal from the root directory of your project :
- install virtualenv and activate our virtualenv
    - ```pip install virtualenv```
    - ```virtualenv env```
    - ```source venv/bin/active```
- install dependencies
    - ```pip install -r requirements.txt```

### Deployment

Once you installed all the dependencies, you can :
- run the API with uvicorn, by typing ```uvicorn main:app```
- run the API with your favorite ASGI server

### Contributors

Thanks to TeddiO, as I reused it source code from this project : https://github.com/TeddiO/pySteamSignIn

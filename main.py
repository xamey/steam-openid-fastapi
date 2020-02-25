from fastapi import FastAPI, Depends
from starlette.requests import Request
from steamsignin import SteamSignIn

app = FastAPI()
api_url = "http://127.0.0.1:8000"


@app.get('/login')
async def main(steam_signin: SteamSignIn = Depends(SteamSignIn)):
    url = steam_signin.ConstructURL(api_url+'/processlogin')
    return steam_signin.RedirectUser(url)


@app.get('/processlogin')
async def pr(request: Request, steam_signin: SteamSignIn = Depends(SteamSignIn)):
	return steam_signin.ValidateResults(request.query_params)
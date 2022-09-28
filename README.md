# Tesla_API_Lite

If you are like me and absolutely paranoid about giving api access of your tesla to a third party, these scripts should help you to get started with your own tesla api calls using python. I spent ages trying to find a simple reference that I could reliably check to make sure there was nothing nefarious hidden away in code. But most api's on github focus on a full implementation of the api, far too complicated to check if you are paranoid about your tesla credentials and just trying to get started.

So the objective of this project is provide the absolute bare minimum python code that is as readable as possible (no error checking), clear that there is nothing hidden away and can be used as a starting point for you to build a custom api library.

The project follows the excellent work carried out by @timdorr who has documented the tesla api here[^1]. The code should be read in conjunction with [^1] to confirm that there is nothing nefarious.

It consists of four simple scripts

- **get_token.py** : Uses tesla's login page to retrieve an api access token and saves it to a local file - keep it safe !!
- **refresh_token.py** : The api access token has a lifetime of 8hrs, so use this script to refresh it and avoid repeat logins into your tesla account
- **write_example.py** : Changes the charge current of your tesla
- **read_example.py** : Reads the charge current of your tesla

These scripts can then be used as the basis for any other api call as documented in [^1]

## API Authentication
It is difficult to programatically login to the Telsa API to authenticate and retrieve the api access token. Tesla has firewall checks for bots, and are constantly changing the login process so script longetivity is poor. It is therefore better to manually login to Tesla's own human authentication webpage so the token retreival process always remains current.

The following procedure is needed to securely login to your account using **get_token.py**. Note : This manual procedure is only needed once.

**get_token.py** generates a Tesla token request URL. Copy this link into URL bar of a web browser of your choice (e.g. Chrome, Edge, Firefox....) [as indicated by the red box in the screenshot below]. This will take you to a tesla login page. Login using your tesla account with 2 factor authentication if you have it enabled. You can satisfy yourself that this is a bonafide Tesla URL and you will only pass your login details to Tesla. 

<p align="center"> <img src='https://github.com/Marky0/tesla_api_lite/blob/main/doc/tesla_login.jpg' width="500" height="300"></p>

Upon login, you will be redirected to a 'page not found'. The resulting URL provides a code that can be used to retrieve your api access token. Manually copy the URL [highlighted by the green box in the screenshot below] back into **get_token.py** prompt. Your access token will then be requested and saved to a local file *tesla_token.json*

<p align="center"> <img src='https://github.com/Marky0/tesla_api_lite/blob/main/doc/tesla_auth.jpg' width="500" height="300"></p>

## API token refresh

The access token only remains live for 8hrs. To avoid the nausea of repeating the manual login procedure if the token has expired, Tesla provide a method for refresh. Use **refresh_token.py** if it has been more than 8hrs since your last api call to retrieve a new access token.

## read and write api calls

Two simple scripts are provided which then give an example of how to read and set the charging current for your tesla. These scripts can then be used as the basis for any other api call as documented in [^1]

[^1]: https://tesla-api.timdorr.com/

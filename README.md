# tesla_api_lite
If you are like me and absolutely paranoid about giving api access of your tesla to a third party, these scripts should help you to get started with your own tesla api calls using python. I spent ages trying to find a simple reference that I could reliably check to make sure there was nothing nefarious hidden away in code. But most api's on github focus on a full implementation of the api, far too complicated to check if you are paranoid about your tesla credentials and just trying to get started.
So the objective of this project is provide the absolute bare minimum python code that is as readable as possible (no error checking), clear that there is nothing hidden away and can be used as a starting point for you to build a custom api library.

The project follows the excellent work carried out by @timdorr who has documented the tesla api here :  https://tesla-api.timdorr.com/

It consists of three simple scripts

     get_token.py : Uses tesla's login page to retrieve an api access token and saves it to a local file - keep it safe !!
     
     refresh_token.py : The api access token has a lifetime of 8hrs, so use this script to refresh it and avoid repeat logins into your tesla account
  
     write_example.py : Changes the charge current of your tesla
  
     read_example.py : Reads the charge current of your tesla

These scripts can then be used as the basis for any other api call as documented in https://tesla-api.timdorr.com/

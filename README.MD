# IG Suite

### Requirements
* Python 3.7
* pipenv

## Dependencies (should be installed via pipenv)
* PyQt5
* [instabot](https://github.com/instagrambot/instabot)
* [fbs](https://build-system.fman.io/)

##### In Terminal
1. Run ```pipenv install``` then run ```pipenv shell```
2. Run ```fbs run```

### Upload picture
1. Click Login, enter your credentials. If Popup window dismisses: Login was successful, else if warning alert pops up: login failed
2. Click Open Images, choose image
3. (Optional) Write your caption
4. Click Upload
5. Scheduled upload: Click scheduled upload, choose date and time and confirm. Don't close the application!
6. Check if the upload was successful. If picture wasn't uploaded then the aspect ratio might not be supported by the API

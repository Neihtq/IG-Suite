from instabot import Bot

WIDTH = 1080
HEIGHT = 1350

class InstagramLib(Bot):

    def __init__(self, username, password):
        super(InstagramLib, self).__init__()
        if self.login(username=username, password=password):
            print("Login successfully")

    def upload(self, photo, caption):
        result = self.upload_photo(photo, caption=caption)
        if result:
            print("upload sucessful!")
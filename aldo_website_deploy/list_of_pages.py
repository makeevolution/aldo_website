from os import listdir
from os.path import isfile, join

mypath="C:/Users/Hp/OneDrive/pythonanywhere/aldo_website_deploy/templates"
onlyfiles = [f for f in listdir(mypath) if f[-4:]=="html"]

print(onlyfiles)



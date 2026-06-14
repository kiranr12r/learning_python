import os

#this will ask for the path 
path = "/"

#it will print all the directories that present 
contents = os.listdir(path)

for item in contents:
    print(item)
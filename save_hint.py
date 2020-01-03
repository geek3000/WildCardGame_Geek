import os, pickle

img_hint={}

for level in os.listdir("./img"):
    print("Level: "+level)
    for image in os.listdir("./img"+'/'+level):
        hint=input(image+': ')
        img_hint[image]=hint

print("Save data")
        
pickle.dump(img_hint, open("hint.word", "wb"))

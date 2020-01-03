import os, requests, json, pickle
img_names={}

for level in os.listdir("./img"):
    print("Level: "+level)
    for image in os.listdir("./img"+'/'+level):
        print(image)
        name = image.split('.')[0]
        page=requests.get("https://api.datamuse.com/words?rel_syn="+name).text
        data=json.loads(page)
        img_names[image]=[]
        img_names[image].append(name)
        for item in data:
            img_names[image].append(item['word'])

print("Save data")
pickle.dump(img_names, open("data.word", "wb"))

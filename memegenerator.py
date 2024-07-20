import connections
import random

def random_meme():#change the file path and img format as necessary when deploying the website 
    meme_number = random.randint(0,2)
    file_path = r"\memes\meme"
    img_format = ".png"
    file = file_path + str(meme_number) + img_format
    print(file)
    return(file)


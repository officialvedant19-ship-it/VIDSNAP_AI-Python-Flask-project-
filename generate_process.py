# This file will look for new folder in user_upload and generate reels if they are not already in done folder
import os
from text_to_speech import text_to_speech_file
import time

def text_to_audio(folder):
    with open(f"user_upload/{folder}/desc.txt", "r") as f:
        text = f.read()
    print(text , folder)
    text_to_speech_file(text , folder)

def create_reels(folder):
    print("CR - ", folder)


    
if __name__ == "__main__" :
    
    while True:
        print("Running que....")
    # reads the content inside of done.txt folder and store it to done_folder
        with open("done.txt","r") as f : 
            done_folder = f.readlines()
        
    # strip i.e deleted the extra spaces from done_folder
        done_folder = [f.strip() for f in done_folder] 
        
    # assign the list of names of user_upload folder to var(folders)
        folders = os.listdir("user_upload")
        
    # This function runs (text_to_audio,create_reels) methods from each new folder in user upload folder and save the name of folder after performing operations to done folder the folder that already exist does not goes through creation again
        for folder in folders : 
            if (folder not in done_folder):
                text_to_audio(folder)
                create_reels(folder)
                with open("done.txt","a") as f:
                    f.write(folder + "\n")
    
    
        time.sleep(4)    
        
            
            
                
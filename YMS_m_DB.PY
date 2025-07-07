# youtube_project/final_tyr.py

from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB connection
client = MongoClient("mongodb+srv://username:passwordpy@cluster0.mysaktg.mongodb.net/?retryWrites=true&w=majority")
db = client["ytmanager"]
collection = db["videos"]

def list_videos():
    videos = list(collection.find())
    if videos:
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video.get('name')}, {video.get('time')}")
    else:
        print("Video list is empty.")

def add_video():
    name = input("Add video name: ")
    time = input("Add video time: ")
    collection.insert_one({'name': name, 'time': time})
    print("Video added successfully.")

def update_video():
    videos = list(collection.find())
    list_videos()
    index = int(input("Which no of video you want to update: "))
    if 1 <= index <= len(videos):
        selected_id = videos[index - 1]['_id']
        name = input("Enter new video name: ")
        time = input("Enter new video duration: ")
        collection.update_one({'_id': selected_id}, {'$set': {'name': name, 'time': time}})
        print("Video updated successfully.")
    else:
        print("Invalid input...")

def delete_video():
    videos = list(collection.find())
    list_videos()
    index = int(input("Enter which no of video you want to delete: "))
    if 1 <= index <= len(videos):
        selected_id = videos[index - 1]['_id']
        collection.delete_one({'_id': selected_id})
        print(f"Video {index} deleted successfully.")
    else:
        print("Invalid video number.")

def exit_fun():
    print("\nSuccessfully exited.")
    exit()

def main():
    while True:
        print(" " + "*" * 52)
        print("*                                                    *")
        print("*           $%* Youtube Management System *%$        *")
        print("*                                                    *")
        print(" " + "*" * 52)
        print("\n\n")
        print("Choose an option:")
        print("1. List YouTube videos")
        print("2. Add YouTube video")
        print("3. Update YouTube video")
        print("4. Delete YouTube video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                exit_fun()
            case _:
                print("Invalid input")

if __name__ == '__main__':
    main()

import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://youtubepy:6YIOrX0JVjiHX5KQ@ytmanager.oi0a7.mongodb.net/", tlsAllowInvalidCertificates=True)
# Not a good idea using this approach, you have to create .env file to store this client
# tlsAllowInvalidCertificates=True not a good way to handel ssl certificate

# DB name
db = client["ytmanager"]
video_collection = db["videos"]
# print(video_collection)

def list_videos():
    print("**" * 50)
    for video in video_collection.find():
        print(f"\n ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

    print("\n**" * 50)



def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})


def  update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({
        '_id': ObjectId(video_id)
    })


def yt_manager_app():
    while True:
        print("\n Youtube Video Manager App")
        print("1. List all the videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter Your Choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Add a video name: ")        
            time = input("Add a video time: ")        
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter a video_id to be updated: ")        
            name = input("Enter a new video name: ")        
            time = input("Enter a new time: ")        
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter a video_id to be deleted: ")               
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("\n Invalid Choice")


def main():
    try:
        yt_manager_app()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
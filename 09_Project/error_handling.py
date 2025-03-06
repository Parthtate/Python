# Whenever you intereact with database or file handling, there is chance of error, therfore you have to handle error

# suppose file handling

file = open('youtube.txt', 'w')

try:
    file.write("This project about manage you youtube video with saving title and video length")
finally:
    file.close()

# another syntax for same error handing, below syntax automatically handle close() 
# USE for any file
with open('youtube.txt', 'w') as file:
    file.write("YOUTUBE VIDEO'S MANAGER")        
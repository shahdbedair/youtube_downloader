from pytube import YouTube

#link = 'https://www.youtube.com/watch?v=FVq6TYw9WjE&t=262s'
link = input("please enter the video url :")

video = YouTube(link)

#print(f"the video title is:\n{video.title}\n")
#print(f"the video description is:\n{video.description}\n")
#print(f"the video views are:\n{video.views}\n")
#print(f"the video rating is:\n{video.rating}\n")
#print(f"the video duration is:\n{video.length/60} minutes\n")

#print(video.streams)

#for stream in video.streams:
   # print(stream)

#for stream in video.streams.filter(progressive=False):
  #  print(stream)    

#for stream in video.streams.filter(progressive=True,res="720p"):
    #print(stream)

#for stream in video.streams.filter(subtype='mp4'):
  #  print(stream)    

#for stream in video.streams.filter(res='10'):
 #   print(stream)  

#print(video.streams.get_highest_resolution())   

#print(video.streams.get_lowest_resolution())

def finish():
  print("download done ")

video.streams.get_highest_resolution().download(output_path="E:\Documents")
video.register_on_complete_callback(finish())

#from pytube import Playlist

#Playlist_link = input("please enter the playlist link :")
#Playlist = Playlist(Playlist_link)

#for video in Playlist.videos:
  #  video.streams.get_highest_resolution().download(output_path="E:")
 #   video.register_on_complete_callback(finish())
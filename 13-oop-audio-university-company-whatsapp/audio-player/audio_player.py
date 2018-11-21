#%%
class Song: 
    
    def __init__(self, name):
        self.name = name
        
    def play(self): 
        print("Now playing: " + self.name)
        

class Album: 
    
    songs = []
    
    def __init__(self, name):
        self.name = name
        
    def add_song(self, song): 
        self.songs.append(song)
        
    def add_songs_list(self, msongs_list): 
        self.songs += songs_list
        
    def play(self): 
        for song in self.songs:
            
            song.play()


steel = Album("Steel")

songs = [
        Song("Red"),
        Song("Rock"),
        Song("Blue")
        ]


steel.add_songs_list(songs)


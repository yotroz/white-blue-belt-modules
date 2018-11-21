#%%

class Collection: 
    
    albums = []
    
    def __init__(self, albums): 
        self.albums = albums
        
    def search(self, album_name): 
        for album in self.albums: 
            if album.name == album_name: 
                return album 
            

class Album: 
    
    songs = []
    def __init__(self, name, songs): 
        self.name = name         
        self.songs = songs

    def play(self): 
        print("playing " + str(self.name))
        
        for song in self.songs :
            song.play()
                
    
class Song: 
    def __init__(self, name): 
        self.name = name
        
    def play(self): 
        print("playing " + str(self.name))
        

    
    

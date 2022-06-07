class Song:
    """Class to represent a song
    Attributes:
        title (str):The title of the song
        artist (Artist): An artist object representing the songs creator.
        duration (int):The duration of the song in seconds . May be zero
    """

    def __init__(self,title,artist,duration=0):
        
        self.title=title
        self.artist=artist
        self.duration=duration

Song.__init__.__doc__="""
        Song init method 
        Args:
            title (str):Initiate the title attribute
            artist (Artist) : At Artist object representing the song creator
            duration (Optional[int]) : Initial value for the duration attribute will default to zero if not sepcified
        
        """


class Album:
    """
    Class to represent an Album, using it's track list
    
    Attributes:
        name (str): The name of the album
        year (int):The year was album was released
        artist:(Artist):The artist reposible for the album if not specified , the artist will defualt to an artist with the name "Varius Artist"
        tracks (List[Song]) : A list of the songs on the album

    Methods : 
        add_song: Used to add a new song to the album track list
    """

    def __init__(self,name,year,artist=None):
        self.name=name
        self.year=year
        if artist is None:
            self.artst=Artist('Varius Artist')
        else:
            self.artist=artist
        self.track=[]


    def add_song(self,song,position=None):
        """
        Add song to track list

        Args:
            song (Song) : A song to add
            position (Optional[int]): If sepcified , the song will be added to that position in the track list -inserting it between other song if neccessary Otherwose, the song will bee added to the end of the list
        """

        if position is None:
            self.track.append(song)
        else:
            self.track.insert(position,song)


class Artist:
    """
    Basic class to store artist detials
    
    Attributes:
        name (str): The name of the artist
        album (List(Album)):A list of the albums by this artist
            The List incliudes only those albums in this collection , it is 
            not an exhastive list of artist published album
    
    Method:
        add_album : Use to add a new album to the artist album list

    """

    def __init__(self,name):
        self.name=name
        self.album=[]


    def add_album(self,album):
        """
        Add a new album to the list

        Args:
            album(Album) : Album object to add to the list
                        if the album is alreday present , it will not added again (although this is yet to implemented)

        """
        self.album.append(album)


def find_object(field,object_list):
    """Check 'object_list' to see if an object with a 'name' attribute euqal to 'field' exists , return it if so."""
    for item in object_list:
        if item.name==field:
            return item
    return None



def load_data():
    new_artist=None
    new_album=None
    artist_list=[]

    with open('albums.txt',mode='r') as albums:
        for line in albums:
            #data row should consist of (artist , album , year ,song)

            artist_field,album_field,year_field,song_field=tuple(line.strip('\n').split('\t'))
            year_field=int(year_field)
            print('{}:{}:{}:{}'.format(artist_field,album_field,year_field,song_field))

            if new_artist is None:
                new_artist=Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name!=artist_field:
                #We've just read detail for a new artist
                # store the current album in the current artist collection then create a new artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist=Artist(artist_field)
                new_album=None

            if new_album is None:
                new_album=Album(album_field,year_field,new_artist)
            elif new_album.name!=album_field:
                #We've just read a new album for the current artist
                #Store the current album in the artist collection then create a new album object
                new_artist.add_album(new_album)
                new_album=Album(album_field,year_field,new_artist)


            #create a new song object and add it to the current album collection
            new_song=Song(song_field,new_artist)
            new_album.add_song(new_song)
        #After reading the last line of the text file , we'll have an artist and album that haven't been store -process them now
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)


    return artist_list

def create_check_file(artist_list):
    """Create a check file from the object data for comparision with the original file"""
    with open('checkfile.txt',mode='w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.album:
                for new_song in new_album.track:
                    print('{0.name}\t{1.name}\t{1.year}\t{2.title}'.format(new_artist,new_album,new_song),file=checkfile)



if __name__=='__main__':
    artist=load_data()
    print('There are {} artists'.format(len(artist)))

    create_check_file(artist)







    

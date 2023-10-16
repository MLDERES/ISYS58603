from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, joinedload

# Database setup
DATABASE_URL = "sqlite:///examples/chinook.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FastAPI setup
app = FastAPI(
    title="Chinook API",
    description="API for the Chinook music store",
    version="0.1",
)
# CORS setup (cross-origin scripting)
origins = [
    "http://localhost:8081",
    "file://", # Replace with the port your frontend is running on
]

#  This is required to allow scripts to be called from ports other than the one we are exposing the API on
app.add_middleware(
    CORSMiddleware,
    # This is not a great idea in production, but it's fine for development
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQLAlchemy models
class Track(Base):
    '''
    Class to represent the Track table in the Chinook database
    '''
    __tablename__ = 'tracks'
    trackId = Column("TrackId", Integer, primary_key=True, index=True)
    name = Column(String)
    albumId = Column("AlbumId", Integer, ForeignKey('albums.AlbumId'))
    mediaTypeId = Column("MediaTypeId",Integer, ForeignKey('media_types.MediaTypeId'))
    genreTypeId = Column("GenreId", Integer, ForeignKey('genres.GenreId'))
    composer = Column(String)
    milliseconds = Column(Integer)
    bytes = Column(Integer)
    unit_price = Column("UnitPrice",Integer)

    # Relationships
    album = relationship("Album", back_populates="tracks")
    media_type = relationship("MediaType", back_populates="tracks")
    genre = relationship("Genre", back_populates="tracks")


class Album(Base):
    '''
    Class to represent the Album table in the Chinook database
    '''
    __tablename__ = 'albums'
    albumId = Column("AlbumId", Integer, primary_key=True, index=True)
    artistId = Column("ArtistId",Integer, ForeignKey('artists.ArtistId'))
    title = Column(String)

    # Relationship with Track
    tracks = relationship("Track", back_populates="album")
    artist = relationship("Artist", back_populates="albums")
    
class Artist(Base):
    '''
    Class to represent the Artist table in the Chinook database
    '''
    __tablename__ = 'artists'
    artistId = Column("ArtistId", Integer, primary_key=True, index=True)
    name = Column(String)
    
    # Relationship with Album
    albums = relationship("Album", back_populates="artist")
    
class MediaType(Base):
    '''
    Class to represent the MediaType table in the Chinook database
    '''
    __tablename__ = 'media_types'
    mediaTypeId = Column("MediaTypeId", Integer, primary_key=True, index=True)
    name = Column(String)
    
    # Relationship with Track
    tracks = relationship("Track", back_populates="media_type")

class Genre(Base):
    '''
    Class to represent the Genre table in the Chinook database
    '''
    __tablename__ = "genres"
    name = Column(String)
    genreId = Column("GenreId", Integer, primary_key=True, index=True)
    
    # Relationship with Track
    tracks = relationship("Track", back_populates="genre")

###
# FastAPI routes
###
@app.get("/tracks/")
def read_tracks(skip: int = 0, limit: int = 10, band: str = None, name: str = None, genre: str = None):
    '''
    ## Get the list of tracks
    
    - **skip**:  The number of tracks to skip
    - **limit**: The number of tracks to return
    - **band**:  The band name to filter by
    - **name**:  The track name to filter by
    - **genre**: The genre to filter by
        
    '''
    db = SessionLocal()
    track_query = db.query(Track).join(Album).join(Artist).join(Genre)
    if band:
        track_query = track_query.filter(Artist.name.like(f"%{band}%"))
    if name:
        track_query = track_query.filter(Track.name.like(f"%{name}%"))
    if genre:
        track_query = track_query.filter(Genre.name.like(f"%{genre}%"))
        
    tracks = track_query.options(joinedload(Track.media_type)).options(joinedload(Track.genre)).offset(skip).limit(limit).all()
    return tracks

@app.get("/albums/")
def read_albums(skip: int = 0, limit: int = 10, include_tracks: bool = False):
    '''
    Get the list of albums, optionally including the track details for each album
    
    - **skip**:  The number of albums to skip
    - **limit**: The number of albums to return
    - **band**:  The band name to filter by
        include_tracks: bool = False
            Whether to include the track details for each album
    '''
    db = SessionLocal()
    album_query = db.query(Album) 
    if include_tracks:
        album_query = album_query.options(joinedload(Album.tracks).joinedload(Track.media_type))
    albums = album_query.offset(skip).limit(limit).all()
    return albums

@app.get("/album/{album_id}/tracks/")
def read_album_tracks(album_id: int):
    '''
    Get the tracks for a given album
    '''
    db = SessionLocal()
    album = db.query(Album).filter(Album.albumId == album_id).first()
    if album:
        # Here we decided to dispense with the unnecessary information and just return the track name, none of the other 
        # details (which would be the default)
        return {"album_title": album.title, "tracks": [track.name for track in album.tracks]}
    else:
        return {"error": "Album not found"}

@app.get("/artists/")
def read_artists(skip: int = 0, limit: int = 10, name: str = None):
    '''
    Get the list of artists
    
    - **skip**:  The number of artists to skip
    - **limit**: The number of artists to return
    - **name**:  The artist name to filter by
    '''
    db = SessionLocal()
    # Start the query
    artist_query = db.query(Artist)
    # If the name parameter was provided then add to the query
    if name is not None:
        artist_query = artist_query.filter(Artist.name.like(f"%{name}%"))
    # Now apply the limit and offset parameters
    artists = artist_query.offset(skip).limit(limit).all()
    return artists

@app.get("/artists/{artist_id}/")
def read_artist(artist_id:int = -9999):
    '''
    Get a particular artist
    '''
    db = SessionLocal()
    artist = db.query(Artist).filter(Artist.artistId == artist_id).first()
    return artist

@app.get("/artists/{artist_id}/albums/")
def read_artist_albums(artist_id: int):
    '''
    Get the albums for a given artist
    '''
    db = SessionLocal()
    artist = db.query(Artist).filter(Artist.artistId == artist_id).first()
    if artist:
        # Now that we found an artist, we can return the albums
        return {"artist_name": artist.name, "albums": [album.title for album in artist.albums]}
    else:
        return {"error": "Artist not found"}
    
@app.post("/artists/")
def create_artist(name: str):
    '''
    Add a new artist
    
    - **name**: The name of the artist
    '''
    db = SessionLocal()
    artist = Artist(name=name)
    db.add(artist)
    # Write the changes to the database
    db.commit()
    new_record = db.query(Artist).filter(Artist.name == name).first()
    return new_record

@app.delete("/artists/")
def delete_artist_by_name(name=None):
    '''
    Remove an artist by name
    
    - **name**: The name of the artist
    '''
    db = SessionLocal()
    if not name:
        return {"error": "No name provided"}
    artist = db.query(Artist).filter(Artist.name.like(f"%{name}%")).first()
    if artist:
        db.delete(artist)
        db.commit()
        return {"message": "Artist deleted", "artist": artist}
    else:
        return {"error": "Artist not found"}
    
@app.delete("/artists/{artist_id}/")
def delete_artist(artist_id: int):
    '''
    Remove an artist by ID
    
    - **artist_id**: The ID of the artist
    '''
    db = SessionLocal()
    artist = db.query(Artist).filter(Artist.artistId == artist_id).first()
    if artist:
        db.delete(artist)
        db.commit()
        return {"message": "Artist deleted"}
    else:
        return {"error": "Artist not found"}

@app.put("/artists/{artist_id}/")
def update_artist(name: str):
    '''
    Change the name of an artist
    
    - **artist_id**: The ID of the artist
    - **name**: The new name of the artist
    '''
    db = SessionLocal()
    artist = db.query(Artist).filter(Artist.artistId == artist_id).first()
    if artist:
        artist.name = name
        db.commit()
        return {"message": "Artist updated"}
    else:
        return {"error": "Artist not found"}
from fastapi import FastAPI
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

# SQLAlchemy models
class Track(Base):
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


class Album(Base):
    __tablename__ = 'albums'
    albumId = Column("AlbumId", Integer, primary_key=True, index=True)
    artistId = Column("ArtistId",Integer, ForeignKey('artists.ArtistId'))
    title = Column(String)

    # Relationship with Track
    tracks = relationship("Track", back_populates="album")
    artist = relationship("Artist", back_populates="albums")
    
class Artist(Base):
    __tablename__ = 'artists'
    artistId = Column("ArtistId", Integer, primary_key=True, index=True)
    name = Column(String)
    
    # Relationship with Album
    albums = relationship("Album", back_populates="artist")
    
class MediaType(Base):
    __tablename__ = 'media_types'
    mediaTypeId = Column("MediaTypeId", Integer, primary_key=True, index=True)
    name = Column(String)
    
    # Relationship with Track
    tracks = relationship("Track", back_populates="media_type")

###
# FastAPI routes
###
@app.get("/tracks/")
def read_tracks(skip: int = 0, limit: int = 10, band: str = None, name: str = None, genre: str = None):
    '''
    ## Get the list of tracks
    
    - **skip**:  The number of albums to skip
    - **limit**: The number of albums to return
    - **band**:  The band name to filter by
    - **name**:  The track name to filter by
        
    '''
    db = SessionLocal()
    track_query = db.query(Track).join(Album).join(Artist)
    if band:
        track_query = track_query.filter(Artist.name.like(f"%{band}%"))
    if name:
        track_query = track_query.filter(Track.name.like(f"%{name}%"))
        
    tracks = track_query.options(joinedload(Track.media_type)).offset(skip).limit(limit).all()
    return tracks

@app.get("/albums/")
def read_albums(skip: int = 0, limit: int = 10, includeTrackDetails: bool = False):
    '''
    Get the list of albums, optionally including the track details for each album
    
    params:
    
        skip: int = 0
            The number of albums to skip
    
        limit: int = 10
            The number of albums to return
    
        includeTrackDetails: bool = False
            Whether to include the track details for each album
    '''
    db = SessionLocal()
    if includeTrackDetails:
        albums = db.query(Album).options(joinedload(Album.tracks).joinedload(Track.media_type)).offset(skip).limit(limit).all()
    else:
        albums = db.query(Album).offset(skip).limit(limit).all()
    return albums

@app.get("/album/{album_id}/tracks/")
def read_album_tracks(album_id: int):
    db = SessionLocal()
    album = db.query(Album).filter(Album.albumId == album_id).first()
    album_tracks = album.tracks
    if album:
        return {"album_title": album.title, "tracks": [track.name for track in album.tracks]}
    else:
        return {"error": "Album not found"}

@app.get("/artists/")
def read_artists(skip: int = 0, limit: int = 10, name: str = None):
    db = SessionLocal()
    artist_query = db.query(Artist)
    if name:
        artist_query = artist_query.filter(Artist.name.like(f"%{name}%"))
    artists = artist_query.offset(skip).limit(limit).all()
    return artists

@app.get("/artist/{artist_id}/albums/")
def read_artist_albums(artist_id: int):
    db = SessionLocal()
    artist = db.query(Artist).filter(Artist.artistId == artist_id).first()
    if artist:
        return {"artist_name": artist.name, "albums": [album.title for album in artist.albums]}
    else:
        return {"error": "Artist not found"}
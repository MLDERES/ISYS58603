from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# Database setup
DATABASE_URL = "sqlite:///examples/chinook.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FastAPI setup
app = FastAPI()

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
def read_tracks(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    tracks = db.query(Track).offset(skip).limit(limit).all()
    return tracks

@app.get("/albums/")
def read_albums(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    albums = db.query(Album).offset(skip).limit(limit).all()
    return albums

@app.get("/album/{album_id}/tracks/")
def read_album_tracks(album_id: int):
    db = SessionLocal()
    album = db.query(Album).filter(Album.id == album_id).first()
    album_tracks = album.tracks
    if album:
        return {"album_title": album.title, "tracks": [track.name for track in album.tracks]}
    else:
        return {"error": "Album not found"}

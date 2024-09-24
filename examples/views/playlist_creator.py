# This is just a simple UI to show how to walk through a text based app
# for creating and modifying playlists using the Chinook data
import os

class Term:
    '''
    This class contains methods for displaying text in different colors
    '''
    # ANSI escape codes for colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'  # Reset to default color

    @classmethod
    def red(cls, text):
        return cls.RED + text + cls.RESET

    @classmethod
    def green(cls, text):
        return cls.GREEN + text + cls.RESET

    @classmethod
    def yellow(cls, text):
        return cls.YELLOW + text + cls.RESET

    @classmethod
    def blue(cls, text):
        return cls.BLUE + text + cls.RESET

    @classmethod
    def magenta(cls, text):
        return cls.MAGENTA + text + cls.RESET
    
    @classmethod
    def clear(cls):
        os.system('clear')

def todo(txt):
    print(Term.blue(f"TODO: {txt}"))
    
def main_menu():
    while True:
        Term.clear()
        print("Welcome to the playlist creator!")
        print(Term.green("1) Create a new playlist"))
        print(Term.green("2) View an existing playlist"))
        print(Term.green("3) Delete a playlist"))
        print(Term.green("4) Exit"))
        choice = input("Enter your choice: ")
        if choice == '1':
            create_playlist()
        elif choice == '2':
            view_playlist()
        elif choice == '3':
            delete_playlist()
        elif choice == '4':
            print(Term.blue("Goodbye!"))
            break
        else:
            print(Term.red("Invalid choice!"))

def create_playlist():
    Term.clear()
    print(Term.magenta('Create a new playlist'))
    print(Term.magenta('---------------------'))
    playlist_name = input('Enter the name of the playlist: ')
    todo("Call the POST /playlists endpoint to create a new playlist.\nStore the playlist id")
    
    song_ids = get_songs(playlist_name)
    todo("Call the PUT /playlists/{playlist_id}/tracks endpoint to add the songs to the playlist")
    

def get_songs(playlist_name):
    
    Term.clear()
    print(Term.magenta(f"Search for songs to add to the playlist: '{playlist_name}'"))
    print(Term.magenta("---------------------------------------"))
    while True:
        song_name =input("Enter a song name to search for: ")
        if song_name == '':
            break
        todo("Call the GET /tracks endpoint to search for songs matching the name")
        todo("Display the results to the user")
        todo("Ask the user to select a song by number")
        todo("Add the *song id* to the collection of songs for the playlist")
    

def view_playlist():
    Term.clear()
    print(Term.magenta("View an existing playlist"))
    print(Term.magenta("-------------------------"))
    play_list_name = input("Enter the name of the playlist to view: ")
    todo("Call the GET /playlists endpoint to search for playlists matching the name")
    todo("Display the results to the user")
    playlist_id = input("Which playlist do you want to view? ")
    todo("Call the GET /playlists/{playlist_id}/tracks endpoint to get the songs for the playlist")
    todo("Display the results to the user")
    input("Press enter to continue")
    

def delete_playlist():
    Term.clear()
    print(Term.magenta("Delete an existing playlist"))
    print(Term.magenta("-------------------------"))
    play_list_name = input("Enter the name of the playlist to delete: ")
    todo("Call the GET /playlists endpoint to search for playlists matching the name")
    todo("Display the results to the user")
    playlist_id = input("Which playlist do you want to delete? ")
    todo("Call the DELETE /playlists/{playlist_id}")
    input("Press enter to continue")
    

if __name__ == '__main__':
    Term.clear()
    main_menu()
    
### API Endpoints
# GET /playlists
# GET /playlists/{playlist_id}
# GET /playlists?name={playlist_name}
# POST /playlists
# PUT /playlists/{playlist_id} (add songs)
# DELETE /playlists/{playlist_id}

# GET /tracks?name={track_name}
# GET /tracks?artist={artist_name}&start={start}&limit={limit}
# GET /tracks?genre={genre_name}&page={page_number}&size={page_size}

# GET /album?name={track_name}
# GET /album?artist={artist_name}&start={start}&limit={limit}
# GET /album?genre={genre_name}&page={page_number}&size={page_size}

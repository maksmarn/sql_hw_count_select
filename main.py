from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")

db.print_tables(verbose=True)


def print_artist_names():
    artist_names = db.execute("SELECT Name FROM Artist")
    print(artist_names)


print_artist_names()


def print_german_billing():
    german_billing = db.execute("SELECT * FROM Invoice WHERE BillingCountry = 'Germany'")
    print(german_billing)


print_german_billing()


def num_of_albums():
    album_count = db.execute("SELECT COUNT(AlbumId) FROM Album")
    print(album_count)


def count_the_french():
    french_count = db.execute("SELECT COUNT (CustomerId) FROM Customer WHERE Country = 'France'")
    print(french_count)


num_of_albums()

count_the_french()

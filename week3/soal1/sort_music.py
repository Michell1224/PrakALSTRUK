songs = [
    {"title": "Golden Hour", "artist": "JVKE", "genre": "Pop", "views": 980000},
    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": "Pop", "views": 2500000},
    {"title": "Snooze", "artist": "SZA", "genre": "R&B", "views": 1200000},
    {"title": "N95", "artist": "Kendrick Lamar", "genre": "Hip-Hop", "views": 850000},
    {"title": "As It Was", "artist": "Harry Styles", "genre": "Pop", "views": 2100000},
    {"title": "Kill Bill", "artist": "SZA", "genre": "R&B", "views": 1750000}
]

def sort_by_views(songs):
    hasil = songs.copy()
    n = len(hasil)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if hasil[j]["views"] < hasil[j+1]["views"]:
                hasil[j], hasil[j+1] = hasil[j+1], hasil[j]
                
    return hasil

def sort_by_favourite_genre(songs, favourite_genre):
    hasil = songs.copy()
    n = len(hasil)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if hasil[j]["genre"] != favourite_genre and hasil[j+1]["genre"] == favourite_genre:
                hasil[j], hasil[j+1] = hasil[j+1], hasil[j]
                
    return hasil

print("=== SORT BY VIEWS ===")

result_views = sort_by_views(songs)

for song in result_views:
    print(song["title"], "-", song["views"], "views")


print("\n=== SORT BY FAVOURITE GENRE ===")

favourite_genre = "R&B"

result_genre = sort_by_favourite_genre(songs, favourite_genre)

for song in result_genre:
    print(song["title"], "-", song["artist"], "-", song["genre"])
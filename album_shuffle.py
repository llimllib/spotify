#!/usr/bin/env python
"""
A script that will print 5 random albums from your saved albums
"""
import random
import sys

# pip install spotipy
import spotipy
import spotipy.util as util


def main():
    scope = "user-library-read"

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print(f"Usage: {sys.argv[0]} <username>")
        sys.exit()

    token = util.prompt_for_user_token(username, scope)
    if not token:
        print("Can't get token for", username)
        sys.exit(1)

    sp = spotipy.Spotify(auth=token)
    albums = sp.current_user_saved_albums()
    allalbums = []
    while albums:
        for item in albums["items"]:
            artists = ", ".join(a["name"] for a in item["album"]["artists"])
            name = item["album"]["name"]
            allalbums.append(f"{artists} - {name}")
        albums = sp.next(albums)

    random.shuffle(allalbums)

    print("\n".join(allalbums[0:5]))


if __name__ == "__main__":
    main()

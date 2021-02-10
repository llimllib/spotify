#!/usr/bin/env python
"""
A script that will print all of the songs in your spotify library that contain
a question mark
"""
import re
import sys

# pip install spotipy
import spotipy
import spotipy.util as util


def main():
    scope = "user-library-read"

    if len(sys.argv) > 1:
        username = sys.argv[1]
        query = sys.argv[2]
    else:
        print("Usage: %s username query" % (sys.argv[0],))
        sys.exit()

    token = util.prompt_for_user_token(username, scope)
    if not token:
        print("Can't get token for", username)
        sys.exit(1)

    matches = []
    sp = spotipy.Spotify(auth=token)
    titles = open("titles.txt", "w")
    results = sp.current_user_saved_tracks()
    print(f"searching {query}")
    while results:
        for item in results["items"]:
            track = item["track"]
            titles.write(f'{track["name"]} - {track["artists"][0]["name"]}\n')
            if re.findall(query, track["name"], re.I):
                matches.append(track)
                print(track["name"] + " - " + track["artists"][0]["name"])
        results = sp.next(results)


if __name__ == "__main__":
    main()

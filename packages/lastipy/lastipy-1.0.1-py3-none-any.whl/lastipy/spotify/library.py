from lastipy.spotify.parse_spotify_tracks import parse_tracks
import spotipy
import logging


#TODO test
def get_tracks_in_playlists(spotify, username):
    """Returns all tracks in the given user's playlists"""

    logging.info("Fetching all tracks in " + username + "'s playlists")

    playlists = spotify.current_user_playlists()['items']

    tracks = []
    for playlist in playlists:
        tracks = tracks + _get_tracks_in_playlist(spotify, username, playlist)

    logging.info("Fetched tracks " + str(tracks))

    return tracks


def _get_tracks_in_playlist(spotify, username, playlist):
    tracks_in_playlist = []

    keep_fetching = True
    while keep_fetching:
        json_response = spotify.user_playlist_tracks(user=username,
                                                   playlist_id=playlist['id'],
                                                   offset=len(tracks_in_playlist))
        if json_response['items']:
            tracks_in_playlist = tracks_in_playlist + parse_tracks(json_response['items'])
        else:
            keep_fetching = False

    return tracks_in_playlist


def get_saved_tracks(spotify, username):
    """Returns the all of the given user's saved tracks"""

    logging.info("Fetching " + username + "'s saved tracks")

    saved_tracks = []
    keep_fetching = True
    while keep_fetching:
        json_response = spotify.current_user_saved_tracks(offset=len(saved_tracks))
        if json_response['items']:
            saved_tracks = saved_tracks + parse_tracks(json_response['items'])
        else:
            keep_fetching = False

    logging.info("Fetched tracks " + str(saved_tracks))

    return saved_tracks

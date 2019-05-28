# wazam-API
Backend for wazam

This is a backend built using flask.
It has one active endpoint /music. This endpoint takes .webm music blob.
Watson speech to text is then used to discover lyrics of what was sung in the music sample. 
These lyrics then pass through the genius API to give the title, artist and picture.
The endpoint return the info from genius along with a link to the song on spotify.

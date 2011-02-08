#!/usr/bin/env python
import gdata.photos.service
import gdata.media
import gdata.geo

gd_client = gdata.photos.service.PhotosService()
# Fill these in with your Google email and password.
gd_client.email = ""
gd_client.password = ""
gd_client.source = ""
gd_client.ProgrammaticLogin()

def upload(filename, album=None, comment=None):
    newalbum = True
    if album:
        albums = gd_client.GetUserFeed(user=gd_client.email)
        for alb in albums.entry:
            if album == alb.title.text:
                album = alb
                print "album exists", type(album)
                newalbum = False
                break

        if newalbum:
            album = gd_client.InsertAlbum(title=album, summary="")


    album_url = '/data/feed/api/user/%s/albumid/%s' % (gd_client.email,
                                                       album.gphoto_id.text)
    if comment == None:
        comment = ""

    ext = filename.split(".")[-1].lower()
    if ext == "png":
        content_type = "image/png"
    elif ext == "jpg" or ext == "jpeg":
        content_type = "image/jpeg"

    return gd_client.InsertPhotoSimple(album_url, filename,
            comment, filename, content_type=content_type)

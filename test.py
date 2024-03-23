from access2base import *
import os


def file_to_url(event):
    fsfield = event.Source.Model
    form = fsfield.Parent
    hfield = form.getByName("File Path")
    url = fsfield.Text
    if url is not None:
        try:
            if os.path.exists(url):
                sturl = Basic.ConvertToUrl(url)
                hfield.Value = sturl
        except FileNotFoundError:
            msg = "File Not Found: {}".format(url)
            Basic.MsgBox(msg, 0, "Error")

from access2base import *
import os


def console():
    TraceConsole()


def file_to_url(event):
    # Macro to retrieve path from FileSelectionField and write to bound HiddenField
    Application.OpenConnection()
    form = Application.Forms("Game-by-Record")
    fsfield = form.Controls("ROM File Selector")
    hfield = form.Controls("File Path")
    url = fsfield.Text
    if url is not None:
        try:
            if os.path.exists(url):
                sturl = Basic.ConvertToUrl(url)
                hfield.Value = sturl
        except FileNotFoundError:
            msg = "File Not Found: {}".format(url)
            Basic.MsgBox(msg, 0, "Error")
    Application.CloseConnection()


def reset_between_records(event):
    # Macro to clear value of FileSelectionField when changing records
    Application.OpenConnection()
    form = Application.Forms("Game-by-Record")
    fsfield = form.Controls("ROM File Selector")
    if fsfield.Text and fsfield.Value is not None:
        fsfield.Value = ""
    Application.CloseConnection()


def diplay_on_load(event):
    # Macro to update value of FileSelectionField with bound value from HiddenField
    Application.OpenConnection()
    form = Application.Forms("Game-by-Record")
    fsfield = form.Controls("ROM File Selector")
    hfield = form.Controls("File Path")
    fsfield.Value = hfield.Text
    Application.CloseConnection()

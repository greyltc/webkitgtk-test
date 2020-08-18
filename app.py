#!/usr/bin/env python3

import gi
gi.require_version("WebKit2", "4.0")
#gi.require_version("Gtk", "3.0")
#gi.require_version("Gdk", "3.0")
#from gi.repository import GLib, Gio, Gtk, Gdk, Pango


#import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository.WebKit2 import WebView#, Settings


builder = Gtk.Builder()
builder.add_from_file("layout.glade")

webview = builder.get_object("wv")
webview.load_uri("https://duckduckgo.org/")

window = builder.get_object("top")
window.show_all()

Gtk.main()
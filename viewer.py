#!/usr/bin/python
from gi.repository import WebKit
from gi.repository import Gtk
from gi.repository import GObject
import os


class VentanaBoton(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Notificador de novedades Ceibal")
        self.create_button()
    
        self.set_decorated(False)
        self.move(950,20)
        self.set_accept_focus(False)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def create_button(self):
        self.button = Gtk.Button(label="Novedades")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        visor = Visor().get()


    def get(self):
        return self




class Visor(Gtk.Window):
 
    def __init__(self):
        GObject.threads_init()
        Gtk.Window.__init__(self, title="Visor de novedades Ceibal")

        # Decorators
        self.set_decorated(False)

        self.resize(400,300)
        self.move(900,20)
        self.set_accept_focus(False)
        
        self.hbar = HeaderBar(self)
        self.wviewer = WebViewer(self)

    def get(self):
        self.show_all()
        return self

class Messages:
    wdir = os.path.dirname(os.path.abspath(__file__))
        
    def get_first_unread(self):
        return ('file://' + os.path.join(Messages.wdir, 'message.html'))
    
    def get_next(self):
        return ('file://' + os.path.join(Messages.wdir, 'message.html'))


class WebViewer:

    def __init__ (self,win):
        msg = Messages()
        view = WebKit.WebView()
        view.open(msg.get_first_unread())
        win.add(view)


class HeaderBar:
    
    def __init__(self, win):
        self.box = Gtk.Box(spacing=6)
        win.add(self.box)

        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Goodbye")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

    def on_button1_clicked(self, widget):
        print("Hello")

    def on_button2_clicked(self, widget):
        print("Goodbye")            



win = VentanaBoton().get()
Gtk.main()

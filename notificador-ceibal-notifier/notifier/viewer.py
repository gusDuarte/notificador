#!/usr/bin/python
from gi.repository import WebKit
from gi.repository import Gtk
from gi.repository import GObject
import os

import datetime
import time
from ceibal.notifier import env
from ceibal.notifier.data_base import Db
from ceibal.notifier.utilidades import *
from ceibal.notifier.constantes import DB_FILE,IMAGEN_NOTOFY,BTN_GENERAL,BTN_LINK,TIME_ENTRE_MSJ, TIME_ESPERA, FUNCIONES_PRIORIDAD



class Messages:
    def __init__(self):
        self.db_filename=os.path.join(env.get_data_root(),DB_FILE)        
        self.wdir = os.path.dirname(os.path.abspath(__file__))
    
    def get_first_unread(self, args={}):
        db = Db(self.db_filename)
        messages = filter(self._date_valid,db.get_messages(args))
        return messages
    
    def get_test_message(self):
        return ('file://' + os.path.join(self.wdir, 'message.html'))


    def _date_valid(self,message):
        '''
        @param message: Mensaje a validar.
        
        @summary: Valida si el mensaje ya expiro.
        
        @return: Verdadero si esta vigente el mensaje.
        '''
        expires = message["vencimiento"]
        today = datetime.datetime.strftime(datetime.date.today(), "%Y-%m-%d")
        return today <= expires





class VentanaBoton(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Notificador de novedades Ceibal")
        self.create_button()
    
        #self.set_decorated(False)
        self.move(950,20)
        self.set_accept_focus(False)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        Gtk.main()

    def create_button(self):
        self.button = Gtk.Button(label="Novedades")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        visor = Visor()




class Visor(Gtk.Window):
 
    def __init__(self):
        #GObject.threads_init()
        Gtk.Window.__init__(self, title="Visor de novedades Ceibal")

        # Decorators
        self.set_decorated(False)

        self.resize(400,300)
        self.move(900,20)
        self.set_accept_focus(False)
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box) 
        self.hbar = HeaderBar(self)
        self.wviewer = WebViewer(self)
        self.show_all()



class WebViewer:

    def __init__ (self,win):
        msg = Messages()
        view = WebKit.WebView()
        view.load_string(msg.get_first_unread()[0]['html'], 'text/html', 'UTF-8','/')
        #view.open(msg.get_test_message())
        win.box.pack_start(view, True, True, 0)


class HeaderBar:
    
    def __init__(self, win):
        tb = Gtk.Toolbar()
        tb.set_style(Gtk.ToolbarStyle.ICONS)
        self.win = win
        self.win.box.pack_start(tb, False, False, 0)
        
        self.back = Gtk.ToolButton(Gtk.STOCK_GO_BACK, label="Anterior")
        self.back.connect("clicked", self.on_back_clicked)
        
        self.next = Gtk.ToolButton(Gtk.STOCK_GO_FORWARD,label="Siguiente")
        self.next.connect("clicked", self.on_next_clicked)
        
        self.close = Gtk.ToolButton(Gtk.STOCK_CLOSE,label="Cerrar")
        self.close.connect("clicked", self.on_close_clicked)
        
        sep = Gtk.SeparatorToolItem()

        sep.props.draw = False
        sep.set_expand(True)

        tb.insert(self.back, 0)
        tb.insert(self.next, 1)
        tb.insert(sep, 2)
        tb.insert(self.close, 3)


    def on_next_clicked(self, widget):
        print("Siguiente")

    def on_back_clicked(self, widget):
        print("Atras")            
    
    def on_close_clicked(self, widget):
        print("Goodbye")            
        self.win.destroy() 


win = VentanaBoton()
Gtk.main()

#! /usr/bin/python

import sys
sys.path.append("/home/gustavo/devel/notification/ceibal/notificador-ceibal-notifier")

from ceibal.notifier.data_base import Db
from ceibal.notifier.constantes import DIC_KEYS

base = Db()

html_txt = "<html><header><body>texto del mensaje ...</body></header></html>"

"""                         ID   VENCIMIENTO  FUNCION     ACCION                       TITULO          TEXTO               TEXTO_HTML  IMAGEN """

base.add_message(DIC_KEYS, ["1", "2015-12-31","general",  "http://www.ceibal.edu.uy" ,"Prueba HTML", "Probando visor html", html_txt  ,"/home/gustavo/devel/notification/ceibal/notificador-ceibal-notifier/etc/notifier/images/planceibal.png"])


#!/usr/bin/env python
# coding: utf-8

APPNAME = u"Охуенный блять совет"
URI = 'http://fucking-great-advice.ru/'
API_URI = URI + 'api/random'
SOUND_URI = URI + 'files/sounds'
INTERVAL = 350

from gi.repository import AppIndicator3 as AI
from gi.repository import Gtk
from gi.repository import Notify
from gi.repository import GLib
from gi.repository import GdkPixbuf

import HTMLParser
import urllib2
import json
import signal
import subprocess


main_icon = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" height="145.73" width="146.32" version="1.1">
	<defs>
		<filter id="f4754" color-interpolation-filters="sRGB">
			<feFlood result="flood" flood-color="rgb(0,0,0)" flood-opacity=".8"/>
			<feComposite operator="in" result="c1" in2="SourceGraphic" in="flood"/>
			<feGaussianBlur stdDeviation="5" result="blur"/>
			<feOffset result="offset" dx="4" dy="4"/>
			<feComposite operator="over" result="c2" in2="offset" in="SourceGraphic"/>
		</filter>
		<filter id="f5337" color-interpolation-filters="sRGB">
			<feGaussianBlur stdDeviation="2.46"/>
		</filter>
		<radialGradient id="rg5354" gradientUnits="userSpaceOnUse" cy="536.07" cx="349.43" gradientTransform="matrix(1,0,0,0.95317735,0,25.099999)" r="47.963">
			<stop stop-color="#fff" stop-opacity="" offset=""/>
			<stop stop-color="#000" stop-opacity="" offset=".83"/>
			<stop stop-color="#000" stop-opacity=".234375" offset=".94"/>
			<stop stop-color="#000" stop-opacity=".26953125" offset="1"/>
		</radialGradient>
	</defs>
	<g transform="translate(-298.88474,-453.31859)">
		<g transform="translate(24.913381,-4.4074887)">
			<g filter="url(#f4754)" transform="translate(14.75,11.75)">
				<path fill="#3b00fd" d="m329.8,522.1-44.2,35.7c11.2,13.3,28,21.8,46.8,21.8,0.8,0,1.6-0,2.4-0.1l-5-57.4z"/>
				<path fill="#58ff00" d="m272.2,509c-0.5,3.2-0.8,6.5-0.8,9.8,0,14.8,5.3,28.4,14.2,39l44.2-35.7-57.6-13.1z"/>
				<path fill="#faff10" d="m325.3,458.5c-27.1,3.1-48.8,23.9-53.1,50.5l57.6,13.1-4.5-63.6z"/>
				<path fill="#f18417" d="m332.4,458.1c-2.4,0-4.7,0.1-7.1,0.4l4.5,63.6,48.4-43.3c-11.2-12.7-27.5-20.7-45.8-20.7z"/>
				<path fill="#ee2a18" d="m378.2,478.8-48.4,43.3,59.2,19.3c2.8-7,4.4-14.6,4.4-22.5,0-15.3-5.7-29.3-15.2-40z"/>
				<path fill="#f400ff" d="m329.8,522.1,5,57.4c24.6-1,45.5-16.5,54.2-38.1l-59.2-19.3z"/>
			</g>
			<path fill="url(#rg5354)" d="m397.4,536.1c0,25.2-21.5,45.7-48,45.7s-48-20.5-48-45.7,21.5-45.7,48-45.7,48,20.5,48,45.7z" transform="matrix(1.2711604,0,0,1.3281346,-97.048899,-181.37828)"/>
			<path fill="#fff" fill-opacity=".9" opacity=".9" d="m345.1,475.1c-30.3,0-54.9,24.5-54.9,54.7,0,5.1,0.7,10.1,2.1,14.8,0-17.7,6.9-33.8,18.1-45.8,0.1-0.1,0.2-0.2,0.3-0.3,1-1.1,2.1-2.2,3.2-3.2,0-0,0.1-0.1,0.2-0.1,12-11,27.9-17.8,45.4-17.8,0.6,0,1.3,0,1.9,0.1-5.1-1.6-10.5-2.4-16.2-2.4z" transform="matrix(0.91450138,0,0,0.91450138,28.413124,44.999011)" filter="url(#f5337)"/>
		</g>
	</g>
</svg>
"""

indicator_icon = """
<svg xmlns="http://www.w3.org/2000/svg" height="145.73" width="146.32" version="1.1">
	<g transform="translate(7.9598432,79.107184)">
		<g opacity=".3" fill="#000" transform="matrix(0.98061384,0,0,1,-120.05336,-57.070842)">
			<path d="M160.2,47.4c-13.1-3-24.7-5.6-25.7-5.9l-1.8-0.4,0.2-0.8c0.7-3.6,2.9-9.7,4.7-13.3,7.2-14.2,19.4-24.6,34.7-29.6,2.9-1,8-2.1,8.2-1.9,0.1,0.1,4,55.4,4,56.7,0,0.4-0.1,0.7-0.2,0.7-0.1-0-10.9-2.5-24.1-5.5z"/>
			<path d="m189.5,50.7c-0-0.1-0.9-12.6-2-27.9-1.4-20.4-1.9-27.8-1.7-28,0.2-0.1,2.5-0.1,5.3-0.1,5.1,0.1,9,0.6,13.1,1.7,5.8,1.5,12.7,4.5,17.9,7.9,4.6,3.1,10.3,8,9.7,8.5-0.1,0.1-9.4,8.4-20.6,18.4-11.2,10-20.7,18.5-21.1,18.8-0.4,0.4-0.7,0.6-0.7,0.5z"/>
			<path d="m218.4,63.6c-14.4-4.7-26.2-8.5-26.1-8.6,0-0,9.7-8.7,21.6-19.3l21.5-19.3,0.7,0.9c4.6,5.8,9,14.9,10.7,22.5,1.4,6.2,1.8,14.7,0.8,21.1-0.7,4.7-2.3,10.9-2.9,11.1-0.1,0-12-3.8-26.4-8.5z"/>
			<path d="m192.4,85.3c-1.2-14-2.2-25.5-2.1-25.5,0.1-0.1,52.4,17,52.6,17.2,0.2,0.2-2.1,4.4-3.8,7.2-5.1,7.9-12.2,14.6-20.5,19.3-6.3,3.6-15.7,6.6-22.1,7.1l-1.9,0.1-2.2-25.4z"/>
			<path d="m183.1,110.7c-12.7-1.5-25.6-7.7-34.3-16.6-1.6-1.7-1.8-1.9-1.5-2.3,0.7-0.7,37.9-30.6,37.9-30.5,0.1,0.1,4.3,48.5,4.3,49.2,0,0.4-0.3,0.4-2.3,0.4-1.3-0-3.1-0.1-4.1-0.2z"/>
			<path d="m142.8,87.2c-2.3-2.9-5.3-8.4-7.1-12.8-1.6-3.9-3-9.3-3.7-14.4-0.4-2.8-0.4-13.2-0.1-13.6,0.2-0.2,7.8,1.5,24.5,5.2,13.3,3,24.4,5.6,24.7,5.7,0.4,0.1-3.4,3.3-18.1,15.2-10.2,8.2-18.8,15.1-19,15.3-0.4,0.3-0.5,0.2-1.2-0.6z"/>
		</g>
		<g transform="matrix(0.98061384,0,0,1,-122.05336,-61.070842)" fill="#dfdbd2">
			<path d="M160.2,47.4c-13.1-3-24.7-5.6-25.7-5.9l-1.8-0.4,0.2-0.8c0.7-3.6,2.9-9.7,4.7-13.3,7.2-14.2,19.4-24.6,34.7-29.6,2.9-1,8-2.1,8.2-1.9,0.1,0.1,4,55.4,4,56.7,0,0.4-0.1,0.7-0.2,0.7-0.1-0-10.9-2.5-24.1-5.5z"/>
			<path d="m189.5,50.7c-0-0.1-0.9-12.6-2-27.9-1.4-20.4-1.9-27.8-1.7-28,0.2-0.1,2.5-0.1,5.3-0.1,5.1,0.1,9,0.6,13.1,1.7,5.8,1.5,12.7,4.5,17.9,7.9,4.6,3.1,10.3,8,9.7,8.5-0.1,0.1-9.4,8.4-20.6,18.4-11.2,10-20.7,18.5-21.1,18.8-0.4,0.4-0.7,0.6-0.7,0.5z"/>
			<path d="m218.4,63.6c-14.4-4.7-26.2-8.5-26.1-8.6,0-0,9.7-8.7,21.6-19.3l21.5-19.3,0.7,0.9c4.6,5.8,9,14.9,10.7,22.5,1.4,6.2,1.8,14.7,0.8,21.1-0.7,4.7-2.3,10.9-2.9,11.1-0.1,0-12-3.8-26.4-8.5z"/>
			<path d="m192.4,85.3c-1.2-14-2.2-25.5-2.1-25.5,0.1-0.1,52.4,17,52.6,17.2,0.2,0.2-2.1,4.4-3.8,7.2-5.1,7.9-12.2,14.6-20.5,19.3-6.3,3.6-15.7,6.6-22.1,7.1l-1.9,0.1-2.2-25.4z"/>
			<path d="m183.1,110.7c-12.7-1.5-25.6-7.7-34.3-16.6-1.6-1.7-1.8-1.9-1.5-2.3,0.7-0.7,37.9-30.6,37.9-30.5,0.1,0.1,4.3,48.5,4.3,49.2,0,0.4-0.3,0.4-2.3,0.4-1.3-0-3.1-0.1-4.1-0.2z"/>
			<path d="m142.8,87.2c-2.3-2.9-5.3-8.4-7.1-12.8-1.6-3.9-3-9.3-3.7-14.4-0.4-2.8-0.4-13.2-0.1-13.6,0.2-0.2,7.8,1.5,24.5,5.2,13.3,3,24.4,5.6,24.7,5.7,0.4,0.1-3.4,3.3-18.1,15.2-10.2,8.2-18.8,15.1-19,15.3-0.4,0.3-0.5,0.2-1.2-0.6z"/>
		</g>
	</g>
	<g transform="translate(-298.88474,-453.31859)"/>
</svg>
"""

def create_icon_from_string(contents):
    loader = GdkPixbuf.PixbufLoader()
    loader.write(contents)
    loader.close()
    return loader.get_pixbuf()

parser = HTMLParser.HTMLParser()
temp_icon = '/tmp/fucking-great-advice.png'
pixbuf = create_icon_from_string(main_icon)
indicator_pixbuf = create_icon_from_string(indicator_icon)
indicator_pixbuf.savev(temp_icon, 'png', [], [])
# ~/.config/autostart

def next_advice(foo):
    try:
        response = urllib2.urlopen(API_URI)
        data = json.loads(response.read())
        response.close()
        title = u"%s #%s" % (APPNAME, data['id'])
        text = u"%s" % parser.unescape(data['text'])
        advice = Notify.Notification.new(title, text, None)
        advice.set_icon_from_pixbuf(pixbuf)
        advice.show()
        '''
        if data['sound']:
            subprocess.Popen([ "/usr/bin/mplayer", "%s/%s" % (SOUND_URI, data['sound']) ])
            # "http://translate.google.com/translate_tts?tl=ru&ie=UTF-8&q=" + data['text']
        '''
    except:
        pass
    return True


def build_menu():
    menu = Gtk.Menu()

    item = Gtk.MenuItem('Случайный совет')
    item.connect('activate', next_advice)
    menu.append(item)
    menu.append(Gtk.SeparatorMenuItem())

    '''
    item = Gtk.CheckMenuItem('Включить звук')
    item.set_active(False)
    menu.append(item)
    menu.append(Gtk.SeparatorMenuItem())
    '''

    item = Gtk.MenuItem('Закрыть')
    item.connect('activate', Gtk.main_quit)
    menu.append(item)

    menu.show_all()
    return menu

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Notify.init(APPNAME)
    ai = AI.Indicator.new(APPNAME, temp_icon, AI.IndicatorCategory.APPLICATION_STATUS)
    ai.set_menu(build_menu())
    ai.set_status(AI.IndicatorStatus.ACTIVE)
    GLib.timeout_add_seconds(INTERVAL, next_advice, ai)
    Gtk.main()
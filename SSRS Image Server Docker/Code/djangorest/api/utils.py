from bs4 import BeautifulSoup
from os import listdir
from os.path  import isfile, join
import os
from matplotlib.font_manager import FontProperties

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_translate_string(name ,locale='en'):
    """
        get translated string according to the locale.
    """
    # locale = [x for x in ['en','ch','es','fr','ru']]
    locale_string = locale
    resource_file = __get_resource_file(locale_string)
    if resource_file is None:
        return name
    source = BeautifulSoup(open(resource_file,encoding='utf-8'),"html.parser")

    source_data = source.find_all('data', attrs={'name':name})
    if len(source_data) == 0:
        return name
    else:
        return source_data[0].find('value').text

def get_own_defined_font(locale):
    '''get own defined font. for chinese, the default font can't show.
    '''
    if locale == 'ch':
        fontpath = BASE_DIR + "\\api\\static\\fonts\simsun.ttc"
        if os.path.exists(fontpath): 
            return FontProperties(fname=fontpath, size=12)

    return None

def __get_resource_file(locale='en'):
    static_path = BASE_DIR+"\\api\\static\\locale\\" + locale +"\\"
    if os.path.exists(static_path):
        locale_file = [join(static_path,f) for f in listdir(static_path) if isfile(join(static_path,f))]
        return locale_file[0]
    else:
        return None

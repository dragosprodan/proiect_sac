from xml.dom import minidom
import ssl
import nltk

def import_resources():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

def read_data(filename):
    data_array = []
    mydoc = minidom.parse(filename)
    speakers = mydoc.getElementsByTagName('u')
    for elem in speakers:
        item = elem.getElementsByTagName('seg')
        for aux in item:
            item = aux.firstChild.data.replace('\n','').replace('               ',' ')
            if len(item) > 1:
                data_array.append(item)
    return data_array
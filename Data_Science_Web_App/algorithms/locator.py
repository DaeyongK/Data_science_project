from Data_Science_Web_App.models import TemporaryFile

def locate(key):
    data = None
    pairs = TemporaryFile.objects.all()
    for pair in pairs.iterator():
        if pair.key == key:
            return pair.data
    return data

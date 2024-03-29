
settings = {}

def init(filename):
    if len(settings) == 0:
        with open(filename) as fh: 
            for line in fh:
                line = line.strip()
                if len(line) > 0: 
                    (key,value) = line.split("=")
                    settings[key.strip()] = value.strip()

def get(key):
    if ( not key in settings):
        return None
    
    return settings[key]

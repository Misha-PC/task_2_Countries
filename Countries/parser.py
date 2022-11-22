from json import load



class JsonParser:
    def __init__(self, file="Countries/static/json/countries.json") -> None:
        with open(file, 'r') as fs:
            raw_json = load(fs)
        self.json = {}
        for i in raw_json:
            self.json[i['country']] = i['languages']
            
    def get_all(self):
        return self.json

    def get_countries(self):
        return [i for i in self.json.keys()]
    
    def get_langs(self, country):
        if not country in self.json.keys():
            return None
        
        return self.json[country]
        

parser = JsonParser()


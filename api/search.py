import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def search(keyword,resultSet):
    result = process.extractBests(keyword, resultSet, score_cutoff=50, limit=5)
    return result
        
search("山东大学软件学院",["北京大学软件学院","山东大学经济学院","山东大学软件学院","山大软院"])

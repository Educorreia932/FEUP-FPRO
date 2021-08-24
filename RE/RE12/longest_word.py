import urllib.request

def longest_word(url):
    lengths = {}    
    
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    
    response = urllib.request.urlopen("https://raw.githubusercontent.com/fpro-admin/recitas/master/words")
    words = response.read().decode()
        
    html = set(html.split())
    words = set(words.split())

    result = sorted(html.intersection(words))
   
    for element in result:
        if element not in lengths: 
            lengths[element] = len(element)
            
    return max(lengths, key = lengths.get)
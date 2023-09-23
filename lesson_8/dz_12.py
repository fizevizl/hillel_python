
# def is_palindrom(word):
#     if word.lower()[::-1] == word.lower():
#           return True  
#     return False

def is_palindrom2(word):
    return word.lower()[::-1] == word.lower()

inputdata = ('Країна', 'шалаш', 'Летел', 'вертольот', 'УЧУ', 'мем', 'мова')
palindrom_list = filter(is_palindrom2, inputdata)
result = list(palindrom_list)
print(result)

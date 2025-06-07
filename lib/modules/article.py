#note: i should export this to somewhere
class Article:
    def __init__(self,author,magazine,title):
        self.author=author
        self.magazine=magazine
        self.title=title
        if not isinstance(title,str):
            raise ValueError('It has be a string')
        if not isinstance(5 <= len(title) <=  50):
            raise TypeError('Has to be between 5 and 50 characters')
        
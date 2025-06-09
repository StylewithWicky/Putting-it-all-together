#note: i should export this to somewhere
class Article:
    _all_articles=[]

    def __init__(self,author,magazine,title):
        self.author=author
        self.magazine=magazine
        self.title=title
        Article._all_articles.append(self)

        if not isinstance(title,str) or not (5 <= len(title) <=  50):
            raise ValueError('It has be a string and has to be between 5 and 50 characters')
        
    @classmethod
    def all(cls):
        return cls._all_articles
        
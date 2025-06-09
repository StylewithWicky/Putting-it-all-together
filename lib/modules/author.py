from lib.modules.article import Article

class Author:
    def __init__(self,name):
        if not isinstance(name,str) or not name.strip():
            raise ValueError('Name has to be a string and cannot be empty! ')
        self._name=name
        self._articles=[]
        
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all() if article.author ==self]
    
    def magazine(self):
        return list({article.magazine for article in self._articles})
    

    def add_article(self,magazine,title):
        from lib.modules.author import Article
        article=Article(self,magazine,title)
        self._articles.append(article)
        magazine._articles.append(article)
        return(article)
    
    def topic(self):
        return list({magazine.category for magazine in self.magazine()})

    
        
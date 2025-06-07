#also need to import magazine
class Author:
    def __init__(self,name):
        if not isinstance(name,str) or not name.strip():
            raise ValueError('')
        self._name=name
        self._articles=[]
        
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return self._articles
    
    def magazine(self):
        return list({article.magazine for article in self._articles})
    

    def add_article(self,magazine,title):
        from lib.modules.author import Articles
        article=Articles(self,magazine,title)
        self._articles.append(article)
        magazine._article.append(article)
        return(article)
    
    def topic(self):
        return list({magazine.category for magazine in self.magazine})

    
        
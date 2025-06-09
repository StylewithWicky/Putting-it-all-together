from article import Article
class Magazine:
    def __init__(self,name,category):
        self.name=name
        self.category=category
        self._articles=[]
        if not isinstance(2 <= len(name) <= 16):
            raise ValueError('Name has to be between 2 and 16')
        if not isinstance(name,str) or not  name.strip():
            raise ValueError('Name has to be a string')
        if not isinstance(category,str) or not name.strip():
            raise ValueError('Name has to be a string')
        
        @property
        def articles(self):
            return self._articles
        
        def contributors(self):
            return list({article.contribitors for article in self._articles})
        
        def article_title(self):
            return list({articles.title for article in self._articles})
        
        def contributing_authors(self):
            return list({articles.author for articles in self._articles})

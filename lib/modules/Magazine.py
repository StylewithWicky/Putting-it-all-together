from lib.modules.article import Article

class Magazine:
    def __init__(self,name,category):
        if not isinstance(name,str) or not  name.strip():
            raise ValueError('Name has to be a string')
        
        if not (2 <= len(name) <= 16):
            raise ValueError('Name has to be between 2 and 16')
        
        if not isinstance(category,str) or not name.strip():
            raise ValueError('Name has to be a string')
        
        self.name=name
        self.category=category
        self._articles=[]
        
    @property
    def articles(self):
        return [article for article in Article.all() if article.magazine == self]

        
    def contributors(self):
            return list({article.author for article in self.articles})
        
    def article_title(self):
            return list({article.title for article in self.articles})
        
    def contributing_authors(self):
        author_count = {}
        for article in self.articles:
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        return [author for author, count in author_count.items() if count > 2]

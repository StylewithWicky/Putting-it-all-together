from ..modules.author import Author
from ..modules.Magazine import Magazine

a1 = Author("Octavia Butler")
a2 = Author("George Orwell")

m1 = Magazine("Sci-Fi World", "Science Fiction")
m2 = Magazine("Dystopia Times", "Politics")

# Add articles
a1.add_article(m1, "Parable of the Sower")
a1.add_article(m1, "Kindred")
a1.add_article(m1, "Bloodchild")

a2.add_article(m1, "1984 Revisited")
a2.add_article(m2, "Animal Farm Redux")

# Queries
print(m1.article_titles())            
print(m1.contributors())              
print(m1.contributing_authors())      
print(a1.topic_areas())               
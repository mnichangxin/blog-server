class Article:
    __tablename__ = 'blog_article'
    id = Column(Integer, primary_key=True)
    title = Column(String(length=30))

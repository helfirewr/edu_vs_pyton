from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, Session, relationship, joinedload

DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/sqlalchemy'
engine = create_engine(DATABASE_URI)
Base = declarative_base()

article_tags = Table('article_tags', Base.metadata,
    Column('article_id', Integer, ForeignKey('articles.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    # W relacji "many to many", secondary wskazuje na tabelę łączącą
    # (czasami nazywaną tabelą stowarzyszeń lub tabelą pośrednią),
    # która przechowuje klucze obce obu powiązanych tabel.
    # Tabela łącząca zawiera co najmniej dwa klucze obce, które odnoszą się
    # do głównych kluczy każdej z powiązanych tabel.
    tags = relationship('Tag', secondary=article_tags, back_populates='articles')

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    articles = relationship('Article', secondary=article_tags, back_populates='tags')

Base.metadata.create_all(engine)

def add_article_with_tags(title, content, tag_names):
    with Session(engine) as session:
        article = Article(title=title, content=content)
        for tag_name in tag_names:
            tag = session.query(Tag).filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
            article.tags.append(tag)
        session.add(article)
        session.commit()

def get_all_articles():
    with Session(engine) as session:
        # Używając joinedload, możemy załadować powiązane obiekty w ramach tego
        # samego zapytania SQL, co redukuje liczbę zapytań wymaganych do pobrania
        # wszystkich niezbędnych danych.
        articles = session.query(Article).options(joinedload(Article.tags)).all()
        return articles

def add_tags_if_not_exist(tag_names):
    with Session(engine) as session:
        for tag_name in tag_names:
            if not session.query(Tag).filter_by(name=tag_name).first():
                new_tag = Tag(name=tag_name)
                session.add(new_tag)
        session.commit()

add_tags_if_not_exist(['Python', 'SQL', 'Advanced'])

add_article_with_tags('SQLAlchemy Tutorial', 'Learn SQLAlchemy', ['Python', 'SQL'])
add_article_with_tags('Advanced SQLAlchemy', 'Deep Dive into ORM', ['Python', 'Advanced'])

articles = get_all_articles()
for article in articles:
    tag_names = [tag.name for tag in article.tags]
    print(f"Artykuł: {article.title}, Tagi: {tag_names}")

from app.models import Article, Session

def add_article():
    session = Session()
    name = input("Nombre del artículo: ")
    description = input("Descripción: ")
    amount = int(input("Cantidad: "))
    article = Article(name=name, description=description, amount=amount)
    session.add(article)
    session.commit()
    print("Artículo agregado exitosamente.")

def list_articles():
    session = Session()
    articles = session.query(Article).all()
    for article in articles:
        print(f"{article.id}. {article.name} - {article.amount} ({article.description})")

def edit_article():
    session = Session()
    article_id = int(input("ID del artículo a editar: "))
    article = session.query(Article).get(article_id)
    if article:
        article.name = input(f"Nuevo nombre ({article.name}): ") or article.name
        article.description = input(f"Nueva descripción ({article.description}): ") or article.description
        article.amount = int(input(f"Nueva cantidad ({article.amount}): ") or article.amount)
        session.commit()
        print("Artículo actualizado.")
    else:
        print("Artículo no encontrado.")

def delete_article():
    session = Session()
    article_id = int(input("ID del artículo a eliminar: "))
    article = session.query(Article).get(article_id)
    if article:
        session.delete(article)
        session.commit()
        print("Artículo eliminado.")
    else:
        print("Artículo no encontrado.")
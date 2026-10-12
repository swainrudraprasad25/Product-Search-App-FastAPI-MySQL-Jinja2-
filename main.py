from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from database import base, engine, session

# from mysql.connector import connect
from models import Product

app = FastAPI()
base.metadata.create_all(bind=engine)


# def get_connection():
#     return connect(
#         host="localhost", user="root", password="swain@12345", database="product_db"
#     )


templates = Jinja2Templates(directory="templates")


@app.post("/product", response_class=HTMLResponse)
def showproduct(req: Request, product_name: str = Form()):
    # conn = get_connection()
    # pen = conn.cursor(dictionary=True)
    # pen.execute("select * from product where company like %s",(product_name,))
    # rows=pen.fetchall()

    # conn.close()
    db = session()
    rows = db.query(Product).filter(Product.company == product_name).all()
    return templates.TemplateResponse(
        request=req, name="show_product.html", context={"products": rows}
    )

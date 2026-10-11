from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from mysql.connector import connect

app = FastAPI()


def get_connection():
    return connect(
        host="localhost", user="root", password="swain@12345", database="product_db"
    )


templates = Jinja2Templates(directory="templates")


@app.post("/product", response_class=HTMLResponse)
def showproduct(req: Request, product_name: str = Form()):
    conn = get_connection()
    pen = conn.cursor(dictionary=True)
    pen.execute("select * from product where company like %s",(product_name,))
    rows=pen.fetchall()
  
    conn.close()
    return templates.TemplateResponse(request=req,
                                      name="show_product.html",
                                      context={"products":rows})


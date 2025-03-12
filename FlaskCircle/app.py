from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import asyncio

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/homedelivery'
db = SQLAlchemy(app)


class RetailerProduct(db.Model):
    __tablename__ = 'polls_retailerproduct'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    store_id = db.Column(db.String(120), nullable=False)
    
class Store(db.Model):
    __tablename__ = 'polls_store'

    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    delivery_status = db.Column(db.Boolean, nullable=False)
        

    
        



async def async_function():
    await asyncio.sleep(1)  # simulate an asynchronous task
    return "Async task completed"


async def async_product_db_query():
    """Fetches and returns a list of retailer products sorted by name"""
    ctx = app.app_context()
    ctx.push()
    try:
        products = RetailerProduct.query.all()    
        product_list = [product.name for product in products]
        return {"product_names":product_list}
    finally:
        ctx.pop()

async def async_store_db_query():
    """Fetches and returns a list of retailer products sorted by name"""
    ctx = app.app_context()
    ctx.push()
    try:
        stores = Store.query.all()    
        store_list = [store.name for store in stores]
        return {"store_names":store_list}
    finally:
        ctx.pop()        

@app.route('/')
async def index():
    """
    Index route that waits 1 second and then returns a message
    
    Returns:
        str: A message indicating that an asynchronous task has completed
    """
    result = await async_function()
    return result


@app.route("/get--products-data")
async def get_data():
    data = await async_product_db_query()
    store_data = await async_store_db_query()
    return jsonify(data.update(store_data))

if __name__ == '__main__':
    app.run()
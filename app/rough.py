# Q10 (Scenario):
# Imagine Amazon backend: When a user adds an item to the cart,
#  you need to save the cart data, update stock inventory, and send an email confirmation.
# •	How will you design this flow in FastAPI?
# •	Will you make all requests synchronous or use background tasks?


class User(base):
    id:
    usernmae
    email
    hashed_pasasword
    create_at

class ProducT(BAse)
    id:
    prodcut
    price
    stock
    create_at

class Chart(Base):
    id
    quantiy
    user_id
    profuct_id
    quantiy
    creaet_at

def add_chart(itea_id:int,quantity:int,db:Session=Depends(get_db)):
    product=db.query(Product).filter(ProducT.id === iteam_id).first()
    if not prdocut:
        raise
    cart_itema=Cart(
        id:=1
        quantity=342,
        user_id
    )
    product.stock-=quantity
    db.add(cart_itema)
    db.commit()
    
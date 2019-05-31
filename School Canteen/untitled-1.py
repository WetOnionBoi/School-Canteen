from bottle import run, route, view, get, post, request, static_file
from itertools import count


class Canteen:

    #signifies a private variable. not to be used outside of this class.
    _ids = count (0)

    def __init__(self, food_name, food_image, food_stock, food_price ):
        #not passing ID as we want it to create it.
        self.id = next(self._ids)
        self.name = food_name
        self.image = food_image
        self.stock = food_stock
        self.price = food_price

    #Test Data
food =    [
          Canteen("Sushi Roll pack", "sushdiggity.jpg", 5, "$10"),
          Canteen("Hot dog and Chips", "hotdiggity.jpg",  12, "$8"),
          Canteen("Ham and Cheese Sandwiches", "hamdiggity.jpg", 4, "$5")
          ]

@route("/")
@view("index")
def index():
    #need this function to attach the decorators.
    pass

@route("/menu")
@view("menu")
def Canteen():
    data = dict (menu_list = food)
    return data

@route('/purchase-success/<item_id>', method = 'POST')
@view('purchase-success')
def purchase_success(item_id):
    item_id = int(item_id)
    found_item = None   
    for item in food: 
        if item.id == item_id:
            found_item  = item
    data = dict(item = found_item)
    found_item.stock -= 1   #minus 1 from the amount of items in stock
    return data 
    
@route('/picture/<filename>')
def serve_picture(filename):
    return static_file(filename, root = './Images')

@route("/restock")
@view("restock")
def restock():
    data = dict (menu_list = food)
    return data

@route('/restock/<item_id>', method = 'POST')
@view ('restock-success')
def restock_success(item_id):
    item_id = int(item_id)
    found_item = None
    for item in food:
        if item.id == item_id:
            found_item = item
    data = dict (item = found_item)
    quantity = request.forms.get('quantity')
    quantity = int(quantity)
    found_item.stock += quantity
    return data

run(host='0.0.0.0', port = 8080, reloader=True, debug=True)

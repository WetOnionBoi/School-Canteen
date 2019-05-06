from bottle import run, route, view, get, post, request, static_file
from itertools import count


class Canteen:

    #signifies a private variable. not to be used outside of this class.
    _ids = count (0)

    def __init__(self, food_name, food_stock ):
        #not passing ID as we want it to create it.
        self.id = next(self._ids)
        self.food = food_name
        self.stock = food_stock


    #Test Data
Food =    [
          Canteen("Sushi Roll pack", 5),
          Canteen("Hot dog and Chips",  12),
          Canteen("Ham and Cheese Sandwiches", 4)
          ]

@route("/")
@view("index")
def index():
    #need this function to attach the decorators above.
    pass

run(host='0.0.0.0', port = 8080, reloader=True, debug=True)

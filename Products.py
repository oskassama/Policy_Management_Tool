#souce: https://www.w3schools.com/python/python_classes.asp
#source: https://www.w3schools.com/python/trypython.asp?filename=demo_class_str1
class Products:
    def __init__(self, product_id, product_name, product_description, product_cost, status, deleted):
        self.product_id = product_id
        self.product_name = product_name
        self.product_description = product_description
        self.product_cost = product_cost
        self.status = status #0 = deactive, 1 = active
        self.deleted = deleted #0 = active, 1 = deleted

    #register
    @classmethod
    def create_product(cls, product_id, product_name, product_description, product_cost):
        # create a new product
        # return new product object
        return cls(product_id, product_name, product_description, product_cost, 1, 0)
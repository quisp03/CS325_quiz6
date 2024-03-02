
# s.py

class OrderDetails:
    def __init__(self, customer_info, items, shipping_address):
        self.customerInfo = customer_info
        self.items = items
        self.shippingAddress = shipping_address
        print("Order details Initialized")

class OrderCosts:
    def calculate_total_cost(self, items, taxes, discounts):
        print("Calculated total costs")

class validateOrder:
    def validate_order_data(self, items, customer_address):
        print("Data validated")

class confirmOrder:
    def send_confirmation_email(self, customer_info):
        print("Sent Confirmation")

class updateInventory:
    def update_inventory_levels(self, items):
        print("Updated inventory")


def main():
    get_Details = OrderDetails("customer_info", "items", "shipping_address")
    order_costs = OrderCosts()
    order_costs.calculate_total_cost("items", "taxes", "discounts")
    order_validation = validateOrder()
    order_validation.validate_order_data("items", "customer_address")
    order_confirmation = confirmOrder()
    order_confirmation.send_confirmation_email("customer_info")
    inventory_update = updateInventory()
    inventory_update.update_inventory_levels("items")

if __name__=="__main__":
    main()

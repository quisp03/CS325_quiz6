
# s.py
# The following code is to demonstrate SRP or 'Single Responsibility Principle'
# This principle states that a class should have one sole reason to change.
# In each of the classes, there is only one priority/responsibility in which results in better readility and maintanence.

class OrderDetails:
    # Class responbility is holding order details
    def __init__(self, customer_info, items, shipping_address):
        self.customerInfo = customer_info
        self.items = items
        self.shippingAddress = shipping_address
        print("Order details Initialized")


class OrderCosts:
    # Class responbility is calculating total costs
    def calculate_total_cost(self, items, taxes, discounts):
        print("Calculated total costs")

class validateOrder:
    # Class responbility is validating order
    def validate_order_data(self, items, customer_address):
        print("Data validated")

class confirmOrder:
    # Class responbility is sending confirmation email for orders
    def send_confirmation_email(self, customer_info):
        print("Sent Confirmation")

class updateInventory:
    # Class responbility is updating inventory after an order is made
    def update_inventory_levels(self, items):
        print("Updated inventory")


def main():
    # Assigning variables to approriate data
    # Test functionality
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

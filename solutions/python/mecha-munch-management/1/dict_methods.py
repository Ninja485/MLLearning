"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    for item in items_to_add:
        if current_cart.get(item) is None:
            current_cart[item] = 1
        else:
            current_cart[item] = current_cart[item] + 1
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """
    card_dictionay = dict.fromkeys(notes,1)
    return card_dictionay

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """
    sorted_card = dict(sorted(cart.items()))
    return sorted_card
    
from collections import OrderedDict
def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    processed_dictionay = {}
    for item,number_items in cart.items():
        aisle_info = aisle_mapping.get(item)
        processed_dictionay[item] = [number_items] + aisle_info
    reverse_order_dictionary =  OrderedDict(sorted(processed_dictionay.items(), reverse=True))
    return reverse_order_dictionary


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """
    for key,card_item in fulfillment_cart.items():
        store_item_info = store_inventory.get(key)
        if card_item[0] >= store_item_info[0]:
            store_inventory[key] = ["Out of Stock"] + store_item_info[1:]
        else:
            store_inventory[key] = [store_item_info[0] - card_item[0]] + store_item_info[1:]
    return store_inventory

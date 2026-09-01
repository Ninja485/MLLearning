"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """
    dict = {}
    for item in items:
        if dict.get(item) == None:
            dict[item] = 1
        else:
            dict[item] = dict[item] + 1
    return dict
def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """
    for item in items:
        if inventory.get(item) is None:
            inventory[item] = 1
        else:
            inventory[item] = inventory[item] + 1
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """
    for item in items:
        count_item= inventory.get(item)
        if count_item is not None and count_item > 0:
            inventory[item] = count_item - 1
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """
    inventory.pop(item,"not found")
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """
    tuple_items_list = []
    for key,value in inventory.items():
        if value > 0:
            tuple_items_list.append((key,value))
    return tuple_items_list

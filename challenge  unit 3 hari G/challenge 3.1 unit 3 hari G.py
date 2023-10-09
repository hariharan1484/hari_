def linear_search_product(products, target_product):
    """
    Perform a linear search to find all occurrences of a target product in the list.

    Parameters:
    products (list): List of products to search in.
    target_product (str): Target product name to search for.

    Returns:
    list: List of indices where the target product is found, or an empty list if not found.
    """
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage
product_list = ["Apple", "Banana", "Apple", "Orange", "Apple"]
target_product = "Apple"
result = linear_search_product(product_list, target_product)
print("Indices of", target_product, ":", result)

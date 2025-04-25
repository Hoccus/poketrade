def calculate_cart_total(cart, listings_in_cart):
    total = 0
    for listing in listings_in_cart:
        quantity = cart[str(listing.id)]
        total += listing.price * int(quantity)
    return total

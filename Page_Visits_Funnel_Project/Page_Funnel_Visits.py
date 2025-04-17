import pandas as pd

# |%%--%%| <nl0FItJUP9|DFb8qAxXA2>
r"""°°°
Import all the files
°°°"""
# |%%--%%| <DFb8qAxXA2|6q0wZsHXgS>

visits = pd.read_csv("visits.csv", parse_dates=[1])
cart = pd.read_csv("cart.csv", parse_dates=[1])

checkout = pd.read_csv("checkout.csv", parse_dates=[1])
purchase = pd.read_csv("purchase.csv", parse_dates=[1])

# |%%--%%| <6q0wZsHXgS|o82KOCyhj4>
r"""°°°
Step 1: Inspect the DataFrames using `print` and `head`
°°°"""
# |%%--%%| <o82KOCyhj4|R8q8VhMyor>

print(visits.head(5))
print(cart.head(5))
print(checkout.head(5))
print(purchase.head(5))

# |%%--%%| <R8q8VhMyor|xpHRTUZ2O3>
r"""°°°
Step 2: Left merging visits and cart
°°°"""
# |%%--%%| <xpHRTUZ2O3|aB4nkiHrNy>
# Merge visits and cart into v_to_c dataframe
visits_cart = pd.merge(visits, cart, how="left")
print(visits_cart)

# |%%--%%| <aB4nkiHrNy|ziwdhGTlVQ>
r"""°°°
Step 3: How long is `visits_cart`?
°°°"""
# |%%--%%| <ziwdhGTlVQ|pqM1j77s8y>
# Use len to find out the number of rows in visits_cart
visits_cart_len = len(visits_cart)
print(visits_cart_len)

# |%%--%%| <pqM1j77s8y|cFInl39fiY>
r"""°°°
Step 4: How many timestamps are null for `cart_time`?
°°°"""
# |%%--%%| <cFInl39fiY|OQFh9tTV2o>
# Find number of null rows in cart_time column
cart_time_null = len(visits_cart[visits_cart["cart_time"].isna()])
print(cart_time_null)

# |%%--%%| <OQFh9tTV2o|0wREcQ0fG6>
r"""°°°
Step 5: What percentage only visited?
°°°"""
# |%%--%%| <0wREcQ0fG6|sgkMAQskF4>
# Calculate the percentage of visitors that didn't continue to cart
visitors_didnt_go_to_cart = cart_time_null * 100 / float(visits_cart_len)
print(f"Visitors that didn't add items to their carts: {visitors_didnt_go_to_cart}%")

# |%%--%%| <sgkMAQskF4|2XbMyVl63I>
r"""°°°
Step 6: What percentage placed a t-shirt in their cart but did not checkout?
°°°"""
# |%%--%%| <2XbMyVl63I|r4PZ5WWQOr>
# Perform a left merge on cart and checkout
cart_checkout = pd.merge(cart, checkout, how="left")
print(cart_checkout.head(10))
# Find len of cart_checkout
cart_checkout_len = len(cart_checkout)
print(cart_checkout_len)
# Find number of null in checkout_time column
checkout_time_null = len(cart_checkout[cart_checkout["checkout_time"].isna()])
print(checkout_time_null)
# Calculate the percentage of users who added item to cart, but didnt check out
cart_didnt_go_to_checkout = checkout_time_null * 100 / float(cart_checkout_len)
print(
    f"Users who added item to cart, but did not checkout: {round(cart_didnt_go_to_checkout, 2)}%"
)


# |%%--%%| <r4PZ5WWQOr|Vn5cjdlJo3>
r"""°°°
Step 7: Merge it all together
°°°"""
# |%%--%%| <Vn5cjdlJo3|MWBbtpVpa3>
# Merge visits and cart (already done)
# Merge visits_cart with checkout
visits_cart_checkout = pd.merge(visits_cart, checkout, how="left")
# Merge visits_cart_checkout with purchase
all_data = pd.merge(visits_cart_checkout, purchase, how="left")
print(all_data)

# |%%--%%| <MWBbtpVpa3|WigpUR9I7W>
r"""°°°
Step 8: % of users who got to checkout but did not purchase
°°°"""
# |%%--%%| <WigpUR9I7W|1UY9Crt9d7>
# Calculate the len of checkout (that are not Null)
checkout_time_len = len(all_data[all_data.checkout_time.notna()])
# Calculate the len of purchase (that are not Null)
purchase_time_len = len(all_data[all_data.purchase_time.notna()])

# Calculate the percent of users who entered checkout,
# but did not finalize purchase
checkout_not_purchased = purchase_time_len * 100 / float(checkout_time_len)
print(
    f"Users who entered checkout, but did not finalize purchase: {round(checkout_not_purchased, 2)}%"
)


# |%%--%%| <1UY9Crt9d7|F4wlW7q371>
r"""°°°
Step 9: check each part of the funnel, let's print all 3 of them again
°°°"""
# |%%--%%| <F4wlW7q371|rzj81nU3Nk>
# The weakest part of the funnel is the visitor to cart stage
print(f"Visitors who did not add items to carts: {round(visitors_didnt_go_to_cart), 2}")
print(
    f"Users who added items to cart, but did not check out: {round(cart_didnt_go_to_checkout, 2)}"
)
print(
    f"Users who entered checkout but did not finalize purchase: {round(checkout_not_purchased, 2)}"
)
# Steps to improve this part of the funnel should focus on incentivising users,
# to add products to their carts. One such step might be redesigning the UI,
# enhancing the user experience, and simplifying the process of adding
# products to the cart

# |%%--%%| <rzj81nU3Nk|3fMhsmpAs9>
r"""°°°
*The weakest part of the funnel is clearly getting a person who visited the site to add a tshirt to their cart. Once they've added a t-shirt to their cart it is fairly likely they end up purchasing it. A suggestion could be to make the add-to-cart button more prominent on the front page.*


Step 10: adding new column
°°°"""
# |%%--%%| <3fMhsmpAs9|QcgAlKVxzg>
# Calculate time from initial visit to final purchase, as a column
all_data["time_visit_to_purchase"] = all_data.purchase_time - all_data.visit_time
# |%%--%%| <QcgAlKVxzg|N5dn13NHUH>
r"""°°°
Step 11: examine the results
°°°"""
# |%%--%%| <N5dn13NHUH|koVEWLyChU>
print(all_data.time_visit_to_purchase)

# |%%--%%| <koVEWLyChU|5gaq9NlMS5>
r"""°°°
Step 12: average time to purchase
°°°"""
# |%%--%%| <5gaq9NlMS5|W7YJpOi9yL>
# Calculate the average time between initial visit and final purchase
time_visit_to_purchase_mean = all_data.time_visit_to_purchase.mean()
print(time_visit_to_purchase_mean)


# |%%--%%| <W7YJpOi9yL|OHLZ7dXaDa>

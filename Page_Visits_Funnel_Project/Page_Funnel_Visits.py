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


# |%%--%%| <aB4nkiHrNy|ziwdhGTlVQ>
r"""°°°
Step 3: How long is `visits_cart`?
°°°"""
# |%%--%%| <ziwdhGTlVQ|pqM1j77s8y>


# |%%--%%| <pqM1j77s8y|cFInl39fiY>
r"""°°°
Step 4: How many timestamps are null for `cart_time`?
°°°"""
# |%%--%%| <cFInl39fiY|OQFh9tTV2o>


# |%%--%%| <OQFh9tTV2o|0wREcQ0fG6>
r"""°°°
Step 5: What percentage only visited?
°°°"""
# |%%--%%| <0wREcQ0fG6|sgkMAQskF4>


# |%%--%%| <sgkMAQskF4|2XbMyVl63I>
r"""°°°
Step 6: What percentage placed a t-shirt in their cart but did not checkout?
°°°"""
# |%%--%%| <2XbMyVl63I|r4PZ5WWQOr>


# |%%--%%| <r4PZ5WWQOr|Vn5cjdlJo3>
r"""°°°
Step 7: Merge it all together
°°°"""
# |%%--%%| <Vn5cjdlJo3|MWBbtpVpa3>


# |%%--%%| <MWBbtpVpa3|WigpUR9I7W>
r"""°°°
Step 8: % of users who got to checkout but did not purchase
°°°"""
# |%%--%%| <WigpUR9I7W|1UY9Crt9d7>


# |%%--%%| <1UY9Crt9d7|F4wlW7q371>
r"""°°°
Step 9: check each part of the funnel, let's print all 3 of them again
°°°"""
# |%%--%%| <F4wlW7q371|rzj81nU3Nk>


# |%%--%%| <rzj81nU3Nk|3fMhsmpAs9>
r"""°°°
*The weakest part of the funnel is clearly getting a person who visited the site to add a tshirt to their cart. Once they've added a t-shirt to their cart it is fairly likely they end up purchasing it. A suggestion could be to make the add-to-cart button more prominent on the front page.*


Step 10: adding new column
°°°"""
# |%%--%%| <3fMhsmpAs9|QcgAlKVxzg>


# |%%--%%| <QcgAlKVxzg|N5dn13NHUH>
r"""°°°
Step 11: examine the results
°°°"""
# |%%--%%| <N5dn13NHUH|koVEWLyChU>


# |%%--%%| <koVEWLyChU|5gaq9NlMS5>
r"""°°°
Step 12: average time to purchase
°°°"""
# |%%--%%| <5gaq9NlMS5|W7YJpOi9yL>


# |%%--%%| <W7YJpOi9yL|OHLZ7dXaDa>

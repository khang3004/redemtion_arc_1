transactions = [
    {'id': 1, 'category': 'Electronics', 'price': 1200},
    {'id': 2, 'category': 'Books', 'price': 15},
    {'id': 3, 'category': 'Electronics', 'price': 100}, 
    {'id': 4, 'category': 'Clothing', 'price': 50},
    {'id': 5, 'category': 'Books', 'price': 20},
]

""" #{
    'Electronics': 1300, 
    'Books': 35, 
    'Clothing': 50
} """
def calculate_revenue_by_category(data: list[dict]) -> dict[str, float]:
    revenue_by_category: dict[str, float] = {}
    for tran in data:
        revenue_by_category[tran['category']] = revenue_by_category.get(tran['category'], 0) + tran['price']
    return revenue_by_category
print(calculate_revenue_by_category(transactions))

""" 
# In reality, Data Science data is often "dirty" (Dirty Data). 
# Your the above code assumes the input data is always perfect.

# What happens if a dict is missing the 'category' key? -> Crashes with a KeyError.

# What happens if 'price' is null or a string like '100$'? -> Crashes with a TypeError. 
"""
def calculate_revenue_by_cat_robust(data: list[dict]) -> dict[str, float]:
    revenue_by_cat: dict[str, float] = {}
    # 1. Get data safely
    for tran in data:
        category = tran.get('category')
        price = tran.get('price')
        if category is None or price is None:
            continue
        revenue_by_cat[category] = revenue_by_cat.get(category, 0) + price
    return revenue_by_cat
print(f'Robust Version: {calculate_revenue_by_cat_robust(transactions)}')

#ULTRA VERSION WITH defaultdict 
from collections import defaultdict

def calculate_revenue_clean(data: list[dict]) -> dict[str, float]:
    # Automatically assigns a default value of 0.0 (float) if the key is missing
    revenue: dict[str, float] = defaultdict(float) 
    
    for tran in data:
        revenue[tran['category']] += tran['price']
        
    return dict(revenue) # Convert back to a regular dict when returning
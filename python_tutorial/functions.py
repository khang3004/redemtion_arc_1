def calculate_tax(income: float, tax_rate: float = 0.1) -> float:
    """ Calculate the tax amount based on income and tax rate. 

    Args:
        income (float): The income amount.
        tax_rate (float, optional): The tax rate. Defaults to 0.1.
    
    Returns:
        float: The calculated tax amount.
    """
    return income * tax_rate

print(calculate_tax(income =1000))
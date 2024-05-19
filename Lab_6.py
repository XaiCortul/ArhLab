class PriceCalculator:
	def __init__(self, product_prices):
    	self.product_prices = product_prices

	def calculate_total_price(self, discount=False, tax_rate=0):
    	total_price = sum(self.product_prices)
    	if discount:
        		total_price *= 0.9  # 10% discount
    	else :
        		total_price *= (1 + tax_rate)
    	return total_price
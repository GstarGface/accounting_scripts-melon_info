"""
Prints out all the melons in our inventory
"""

from melons import melon_names, melon_avg_weight, melon_rind_color, melon_flesh_color, melon_seedlessness, melon_prices 


def print_melon(name, weight, rind, flesh, seedless, price):
    with_or_without = 'with'
    if seedless:
        with_or_without = 'without'

    print "%ss weigh %0.1flbs. are %s on the outside, %s on the inside %s seeds and cost $%0.2f" % (name, weight, rind, flesh, with_or_without, price)


for i in melon_names:
    print_melon(melon_names[i], melon_avg_weight[i], melon_rind_color[i], melon_flesh_color[i], melon_seedlessness[i], melon_prices[i])

def melons_dict(): 
	all_melon_data = {}
	for melon in melon_names:
		all_melon_data[melon_names[melon]] = [melon_avg_weight[melon], melon_rind_color[melon], melon_flesh_color[melon], melon_seedlessness[melon], melon_prices[melon]]
	return all_melon_data




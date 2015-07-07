"""
Prints out description of all the melons in our inventory

Then returns a dictionary of all the data on all the melons in the dictionary

(restructured source data) prints all melon data from dictionary of dictionaries 
"""

from melons import melons, melon_names, melon_avg_weight, melon_rind_color, melon_flesh_color, melon_seedlessness, melon_prices 


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

print "*" * 80
print "Inventory Data:"


def print_all_melons(melons_info):
	for melon, specs in melons_info.items():
		print melon 
		for spec, value in specs.items():
			print "%s: %s" % (spec, value)
		print


print_all_melons(melons)

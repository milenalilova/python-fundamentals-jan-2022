materials_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_items = {}
special_item = ''
condition = False


def print_func(materials_dict, junk_items, special_item):
    print(f"{special_item} obtained!")
    print(f"shards: {materials_dict['shards']}")
    print(f"fragments: {materials_dict['fragments']}")
    print(f"motes: {materials_dict['motes']}")
    for mat, qty in junk_items.items():
        print(f"{mat}: {qty}")


while True:
    loot = input().split(' ')
    for i in range(0, len(loot), 2):
        quantity = int(loot[i])
        material = loot[i + 1].lower()
        if material in ['shards', 'fragments', 'motes']:
            materials_dict[material] += quantity
            if materials_dict[material] >= 250:
                if material == 'shards':
                    special_item = 'Shadowmourne'
                elif material == 'fragments':
                    special_item = 'Valanyr'
                elif material == 'motes':
                    special_item = 'Dragonwrath'
                materials_dict[material] -= 250

                print_func(materials_dict, junk_items, special_item)
                condition = True

        else:
            if material not in junk_items.keys():
                junk_items[material] = 0
            junk_items[material] += quantity

        if condition:
            break
    if condition:
        break

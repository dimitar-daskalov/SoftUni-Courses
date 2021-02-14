def stock_availability(inventory_list, command, *args):
    inventory_list = list(inventory_list)
    if command == "delivery":
        items = list(args)
        inventory_list = inventory_list + items
    elif command == "sell":
        if args:
            if isinstance(args[0], int):
                inventory_list = inventory_list[args[0]:]
            elif isinstance(args[0], str):
                items_list = [str(el) for el in args]
                for item in items_list:
                    if item in inventory_list:
                        inventory_list = list(filter(lambda a: a != item, inventory_list))
        else:
            if inventory_list:
                inventory_list = inventory_list[1:]
    return inventory_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))



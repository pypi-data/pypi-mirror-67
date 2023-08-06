import shelve


def shelf_list_contents(shelf_name):
    with shelve.open(shelf_name) as db:
        for k,v in db.items():
            print(k,v)


def shelf_add_item(shelf_name, key, value):
    with shelve.open(shelf_name) as db:
        db[key] = value


def main():
    print("This is a module, it isn't meant to be run directly")

if __name__ == '__main__':
    main()
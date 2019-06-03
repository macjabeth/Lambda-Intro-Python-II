import itertools


class Object():
    new_id = itertools.count().__next__

    def __init__(self, **args):
        self.id = Object.new_id()
        self.replica = args['replica']
        self.name = args['name']
        self.description = args['description']
        self.room_desc = args['room_desc']
        self.weight = args.get('weight')
        self.keywords = (self.replica, *args['aliases'])

    @staticmethod
    def contains(items, thing):
        # last word is most likely the item we need
        # this way we handle cases like `get silver knife`
        thing = thing.split()[-1]
        for item in items:
            if thing in item.keywords:
                return item


class Item(Object):
    def __init__(self, **args):
        super().__init__(**args)
        self.type = 'item'


class CCC(Object):
    def __init__(self, **args):
        super().__init__(**args)
        self.type = 'ccc'

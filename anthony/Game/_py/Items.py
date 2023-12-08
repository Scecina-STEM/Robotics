# global imports

# local imports

# main class
class Item:
    def __init__(self, id:str, name:str, type:str, meta:dict) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.meta = self.Types.returnType(type, meta)
        pass

    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
        yield 'type', self.type
        yield 'meta', dict(self.meta)

        pass

    class Types:
        def returnType(type:str, meta:dict):
            match type:
                case "Weapon": return Item.Types.Weapon(meta)
                case "Object": return Item.Types.Object(meta)
                case "HealthConsumable": return Item.Types.HealthConsumable(meta)
            pass

        class Weapon:
            def __init__(self, meta) -> None:
                self.damage = meta['Damage']
                self.durability = meta['Durability']
                pass

            def __iter__(self):
                yield 'Damage', self.damage
                yield 'Durability', self.durability
        
        class Object:
            def __init__(self, meta) -> None:
                self.b = 1
                pass

            def __iter__(self):
                yield 'b', 1

        class HealthConsumable:
            def __init__(self, meta) -> None:
                self.heals = meta['Heals']
                pass

            def __iter__(self):
                yield 'Heals', self.heals
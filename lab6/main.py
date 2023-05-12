from hash import Hash

COMMANDS = [
    'add ',
    'delete ',
    'value '
]

KEYS = [
        "Ahmed", "Mary", "Alex", "William", "Emila", "Olivia", "James", 
        "Sophia", "Ethan", "Isabella", "Michael", "Emma", "Benjamin", "Ava", 
        "Daniel", "Mia", "Matthew", "Charlotte", "David", "Amelia", "Andrew", 
        "Abigail", "Lucas", "Harper", "Joseph", "Evelyn", "Samuel", "Emily", 
        "Christopher", "Ella", "Jacob", "Grace", "Willy", "Sophie", "Ryan", 
        "Chloe", "Gabriel", "Victoria", "Nicholas", "Zoe", "Luke", "Lily",
        "Nathan", "Lila", "Anthony", "Layla", "Max", "Aria", "Kevin",
        "Avery", "Eric", "Eleanor", "Mark", "Audrey", "Philip", "Hannah",
        "Peter", "Aurora", "Simon", "Bella", "Sean", "Brooklyn", "Henry"
]

VALUES = [
        "BWM E24 635 csi", "Fiat Punto", "Dodge RAM", "Buick Riviera 1965", "Volkswagen Passat B7", "Ford Scorpio",
        "Mini Clubman", "Mazda RX-7", "Mercedes-Benz CLA", "Mercedes-Benz CLS350", "Honda Civic 8", "BMW e63",
        "BMW X7", "Audi A6", "Volkswagen Golf 8", "Dodge Charger", "Toyota Corolla", "Nissan Skyline R34",
        "Peugeot 308", "Subaru Forester", "Subaru Impreza", "Mitsubishi Lancer", "BMW M5 F90",
        "Mazda 636", "Mercedes-Benz Sprinter", "Ford Crown Victoria", "LADA 21031",
        "Porsche Panamera", "Pontiac Firebird", "Ford Probe", "Lincoln Continental",
        "Cadillac Fleetwood", "Chevrolet Corvair", "Chevrolet Camaro",
        "Chevrolet Corvette C6", "Audi Sport quattro",
        "Toyota MarkII X100", "Mitsubishi Galant", "SAAB 9-3",
        "Volvo 200", "AMC Gremlin", "Opel Diplomat",
        "Nissan Z350", "Mercury Marauder", "Rover 75",
        "Alfa Romeo 156", "Land Rover Defender 110", "BMW e65", "Crysler 300M",
        "Lancia Kappa", "Citroen XM", "Jeep Cherokee XJ", "GMC Suburban",
        "Ford Mustang SN95", "Ford Orion Mark2", "Audi A8L", "BMW e90", "Renault Logan",
        "Jaguar XJ", "Nissan Silvia S14", "Toyota Corolla AE86", "Nissan  Maxima A32", "Lancia Delta S4"
]

def main():
    hash_table = Hash()
    for i in range(63):
        hash_table.add_new_hash_line([KEYS[i], VALUES[i]])
    print(hash_table.show_table())
        
    hash_table.delete_element('Daniel')
    hash_table.delete_element('Harper')
    hash_table.delete_element('Philip')

    hash_table.show_table_version_2()

    hash_table.search('Joseph')
    hash_table.search('Brooklyn')
    hash_table.search('Ahmed')
    hash_table.search('Hannah')
    hash_table.search('A')

if __name__ == '__main__':
    main()
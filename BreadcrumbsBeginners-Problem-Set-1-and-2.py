def mad_libs():
    print("Welcome to Mad Libs!")
    
    name = input("Sophia:")
    adjective = input("polite: ")
    verb = input("frolick: ")
    place = input("parks: ")
    food = input("turkey: ")
    vehicle = input("bicycle:")

    story = (
        f"{name} is a very {adjective} person to be around. "
        f"They love to {verb} in {place}. "
        f"Their favourite food is {food} which they eat in a {vehicle}."
    )
    print(story)

def simple_reflex_vacuum(location, status):
    if status == "Dirty":
        return "Clean"

    elif status == "Clean":
        if location == "A":
            return "Move to B"
        else:
            return "Move to A"


print(simple_reflex_vacuum("A", "Dirty"))
print(simple_reflex_vacuum("A", "Clean"))
print(simple_reflex_vacuum("B", "Dirty"))
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
# def model_based_vacuum(location, status, memory):


#     if status == "Dirty":
#         memory[location] = "Clean"
#         return "Clean"


#     if status == "Clean":
#         memory[location] = "Clean"


#     if location == "A":
#         if memory["B"] == "Dirty":
#             return "Move to B"
#         else:
#             return "Do nothing"

#     else:
#         if memory["A"] == "Dirty":
#             return  "Move to A"
#         else:
#             return "Do nothing"


# memory = {
#     "A": "Unknown",
#     "B": "Unknown"
# }

# print(model_based_vacuum("A", "Dirty", memory))
# print(memory)

# print(model_based_vacuum("B", "Clean", memory))
# print(memory)
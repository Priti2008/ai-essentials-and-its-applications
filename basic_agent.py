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
#             return "Move to A"
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
def model_based_vacuum(location, status, memory):


    if status == "Dirty":
        memory[location] = "Clean"
        return "Clean"


    if status == "Clean":
        memory[location] = "Clean"


    if location == "A":
        if memory["B"] == "Dirty":
            return "Move to B"
        else:
            return "Do nothing"

    else:
        if memory["A"] == "Dirty":
            return "Move to A"
        else:
            return "Do nothing"


memory = {
    "A": "Unknown",
    "B": "Unknown"
}

print(model_based_vacuum("A", "Dirty", memory))
print(memory)

print(model_based_vacuum("B", "Clean", memory))
print(memory)
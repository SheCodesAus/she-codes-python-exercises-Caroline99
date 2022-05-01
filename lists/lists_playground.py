# Lists
# 3 elements
# 0 index
# characters = ["a", "b", "c"]
# # print(characters[0], characters[1], characters[2])
# characters.append("d")
# print(characters)
# characters.extend(["e", "f"])
# print(characters)
# characters.insert(1, "g")
# print(characters)
# print(characters.remove("b"))
# print(characters.count("a"))
# print(characters[-1])
# print(characters[0:2])
# print(characters[1:4:2])
# print(characters[2:])
# characters[1]
# characters.pop()
# characters.reverse()
# print(characters)
# characters.sort()
# print(characters)

# if "j" in characters:
#     print("Good")
# else:
#     characters.append("j")
# print(characters)

# print(len(characters))


chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

# indexing
print(len(chilli_wishlist))
# print(chilli_wishlist[4])
print(chilli_wishlist[0])
print(chilli_wishlist[1])
print(chilli_wishlist[-1])
print(chilli_wishlist[0:2])
print(chilli_wishlist[1:3])
chilli_wishlist[1] = 'carrot'

print(chilli_wishlist[2:])
print(chilli_wishlist[-3])

chilli_wishlist.append('dig mat')
chilli_wishlist.extend(['kong', 'tennis ball', 'crocodile toy'])
chilli_wishlist.insert(1, 'peanut butter')
print(chilli_wishlist)
chilli_wishlist.pop()
chilli_wishlist.pop(2)
chilli_wishlist.remove('kong')
print(chilli_wishlist)

if "tennis ball" in chilli_wishlist:
    print("Chilli would like a tennis ball.")
else:
    print("Chilli doesn't feel like playing fetch.")

if len(chilli_wishlist) > 8:
    print("Chilli wants a lot of stuff!")

chilli_wishlist = [
    ['igloo'], #bed
    ['donut toy','tennis ball', 'crocodile toy'], # toys
    ['chicken', 'peanut butter'], # treats
    ['cardboard box', 'kong', 'dig mat'] # activity based toys
]
print(chilli_wishlist[2])
print(chilli_wishlist[2][1])
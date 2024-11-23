s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
fruits = {}
for word in s.split():
    fruits[word] = fruits.get(word, 0) + 1

maximum = max(fruits.values())

f = []

for key, value in fruits.items():
     if value == maximum:
         maximum = value
     if value == maximum:
        f.append(key)

f = [key for key, value in fruits.items() if value == max(fruits.values())]

print(min(f))



    
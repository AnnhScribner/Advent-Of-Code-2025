save_range = []
save_ingredients = []
with open("Dec5/data_base.txt") as file:
    for line in file:
        l = line.strip()

        if "-" in l:
            r = l.split('-')
            r = int(r[0]), int(r[1])
            save_range.append(r)

        else:
            if l != "":
                ing = int(l)
                save_ingredients.append(ing)
    
seen = set()
fresh = 0

for i in range(len(save_ingredients)):
    # print(save_ingredients[i])
    for j in range(len(save_range)):
        range_1 = save_range[j][0]
        range_2 = save_range[j][1]
        if range_1 <= save_ingredients[i] <= range_2 and save_ingredients[i] not in seen:
            fresh += 1
            seen.add(save_ingredients[i])

print(fresh)

def spell_check(values):
    count = 0
    for i in values:
        if i == values[i]:
            count += 1
    return count
values = {"banana":"banana", "apple": "apple", "hypertension":"hypometepher"}

print(spell_check(values))

        

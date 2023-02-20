
# https://www.codewars.com//kata/5a6d3bd238f80014a2000187

def cat_or_dog(years, step):
    old = 0

    for year in range(0, years + 1):

        if year == 15:
            old += 1

        if 15 < year < 24:
            continue

        if year == 24:
            old += 1

        if year > 24 and (year - 24) % step == 0:
            old += 1

    return old


def owned_cat_and_dog(cat_years, dog_years):
    cat_human = cat_or_dog(cat_years, 4)
    dog_human = cat_or_dog(dog_years, 5)

    return [cat_human, dog_human]

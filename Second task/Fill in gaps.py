# https://www.codewars.com//kata/564871e795df155582000013

def fill_gaps(timesheet):

    list_work = []
    works = timesheet.copy()

    work = None

    length = len(works)

    for el in range(length):

        if work is None and works[el] is None:
            continue

        elif works[el] is None:
            list_work.append(el)

        else:
            if works[el] is not work:
                work = works[el]
                list_work.clear()

            else:
                for i in list_work:
                    works[i] = work

    return works

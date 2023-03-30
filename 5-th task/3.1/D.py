while (el := input()) != "":
    
    if el.startswith("##") and not el.endswith("@@@"):
        print(el.strip("##"))
    
    elif not el.endswith("@@@"):
        print(el)
    
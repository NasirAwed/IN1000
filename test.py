#18 poeng

def sjekk_om_fyord(setning, fyord, synonym_liste):
    ordbok = {}
    ordbok_fyord = {}
    for x in setning:
        for elm in synonym_liste:
            for y in elm:
                if y == x:
                    ordbok[y]= elm
                if fyord == y:
                    ordbok_fyord[fyord] = elm
    for key in ordbok:
        if key in ordbok:
            if ordbok[key] == ordbok_fyord[fyord]:
                return True
    return False


print(sjekk_om_fyord("spis masse godsaker", "snop", [["saft","lemonade"],["snacks","snop","godsaker"],["mye","masse"]]))

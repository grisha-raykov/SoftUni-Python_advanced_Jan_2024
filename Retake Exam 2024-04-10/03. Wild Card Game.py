def draw_cards(*args, **kwargs):
    cards_monster = []
    cards_spell = []

    for card_info in args:
        if card_info[1] == "monster":
            cards_monster.append(card_info[0])
        elif card_info[1] == "spell":
            cards_spell.append(card_info[0])

    for card_name, card_type in kwargs.items():
        if card_type == "monster":
            cards_monster.append(card_name)
        elif card_type == "spell":
            cards_spell.append(card_name)

    cards_monster.sort(reverse=True)
    cards_spell.sort()

    result = ""
    if cards_monster:
        result += "Monster cards:\n"
        result += "\n".join(f"  ***{card}" for card in cards_monster)
    if cards_spell:
        if result:
            result += "\n"
        result += "Spell cards:\n"
        result += "\n".join(f"  $$${card}" for card in cards_spell)

    return result
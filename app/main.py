def calculate_team_total_rating(team: list) -> int:
    count = 0
    for item in team:
        count = count + item.get_rating()
    return count


def elves_concert(elves: list) -> None:
    for item in elves:
        item.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for item in dwarves:
        item.eatDwarfBlacksmith()

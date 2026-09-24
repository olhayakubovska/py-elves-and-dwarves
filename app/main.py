def calculate_team_total_rating(team: list) -> int:
    count = 0
    for item in team:
        item.get_rating()
        count = count + item.get_rating()
    return count


def elves_concert(elves: list) -> None:
    for item in elves:
        item.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for item in dwarves:
        item.eat_favourite_dish()

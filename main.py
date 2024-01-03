#!/usr/bin/env python
def get_answer():
    while True:
        user_input = input().strip().lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("Invalid Input Detected! Please enter y/n:")

def get_scroll_type():
    while True:
        scroll_type = input().strip().lower()
        if scroll_type in ["ags", "ss", "prime"]:
            return scroll_type
        else:
            print("Invalid Input Detected! Please enter ags, ss or prime:")

def main():
    # sf stat table
    sf_tyrant_stat = [0, 18, 38, 60, 84, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110]
    sf_tyrant_att = [0, 0, 0, 0, 0, 0, 8, 17, 27, 38, 50, 63, 77, 92, 108, 125]
    sf_arcane_stat = [0, 2, 4, 6, 8, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 55, 70, 85, 100, 115, 130]
    sf_arcane_att = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 29, 45, 62, 80, 99]
    sf_sweetwater_stat = [0, 2, 4, 6, 8, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 53, 66, 79, 92, 105, 118]
    sf_sweetwater_att = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 23, 36, 50, 65, 81]
    sf_superior_stat = [0, 2, 4, 6, 8, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 51, 62, 73, 84, 95, 106]
    sf_superior_att = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 21, 33, 46, 60, 75]
    sf_reinforced_stat = [0, 2, 4, 6, 8, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 49, 58, 67, 76, 85, 94]
    sf_reinforced_att = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 19, 30, 42, 55, 69]
    sf_solid_stat = [0, 2, 4, 6, 8, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 47, 54, 61, 68, 75]
    sf_solid_att = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 17, 27, 38, 50]

    # Welcome dialog
    print("\nYo this is Asleep's MCS Calc I cobbled this shit together so uh yeah\n")

    while True:
        # Variable Declaration
        scroll_stat_value = 0
        scroll_att_value = 0
        is_glove = False
        is_tyrant = False
        is_ghost_ship = False

        # Get Item Level for Starforce Value Check
        print("Please enter the Item's Level: ")
        item_level = int(input())

        # Check if the item is a Glove
        print("Is this item a Glove? Please enter y/n: ")
        is_glove = get_answer()

        if item_level == 150:
            # Check if the item is a Tyrant
            print("Is this item a Tyrant? Please enter y/n: ")
            is_tyrant = get_answer()
            if not is_tyrant and not is_glove:
                # Check if the item is a Ghost Ship Badge
                print("Is this item a Ghost Ship Badge? Please enter y/n: ")
                is_ghost_ship = get_answer()

        # Get Type of Scroll Used
        if not is_ghost_ship:
            print("How is this item scrolled? Please enter ags, ss, or prime.")
            # Calculate added stats from scrolls
            scroll_type = get_scroll_type()
            if scroll_type == "ags":
                scroll_stat_value = 3
                scroll_att_value = 4
            elif scroll_type == "ss":
                if is_glove:
                    scroll_stat_value = 0
                    scroll_att_value = 4
                else:
                    scroll_stat_value = 9
                    scroll_att_value = 0
            elif scroll_type == "prime":
                scroll_stat_value = 10

        # Get Total # of Scrolls used
        print("Please enter the total number of Scrolls used on the item: ")
        total_scroll_count = int(input())

        # Get Current Starforce Value
        print("Please enter the current Star Force of the item: ")
        current_stars = int(input())

        # Get Total Added Stat
        print("Please enter the amount of added desired STAT that you would like to check e.g. if this item has LUK: (10+30), enter 30, not 40: ")
        added_stat_value = int(input())

        # Get Total Added ATT
        print("Please enter the amount of added desired ATT that you would like to check e.g. if this item has ATT: (10+55), enter 55, not 65: ")
        added_att_value = int(input())

        # Get Pre-StarForce Values on clean item
        if 130 <= item_level <= 139:
            added_stat_value -= sf_solid_stat[current_stars]
            added_att_value -= sf_solid_att[current_stars]

        if 140 <= item_level <= 149:
            added_stat_value -= sf_reinforced_stat[current_stars]
            added_att_value -= sf_reinforced_att[current_stars]

        if 150 <= item_level <= 159 and not is_tyrant:
            added_stat_value -= sf_superior_stat[current_stars]
            if not is_ghost_ship:
                added_att_value -= sf_superior_att[current_stars]

        # Special Checker for Tyrants
        if item_level == 150 and is_tyrant:
            added_stat_value -= sf_tyrant_stat[current_stars]
            added_att_value -= sf_tyrant_att[current_stars]

        # Sweetwater Items
        if 160 <= item_level <= 199:
            added_stat_value -= sf_sweetwater_stat[current_stars]
            added_att_value -= sf_sweetwater_att[current_stars]

        # Arcane Umbra Items
        if item_level == 200:
            added_stat_value -= sf_arcane_stat[current_stars]
            added_att_value -= sf_arcane_att[current_stars]

        # In AriesMS, Gloves gain 7 ATT when SF'd from 1-15,
        # gaining att at 1,3,5,7,11,13.
        if is_glove and not is_tyrant:
            extra_glove_att = (min(current_stars, 13) + 1) // 2
            added_att_value = added_att_value - extra_glove_att

        print("\nCalculating MCS...")
        print("Minimum MCS Combination found:")

        if is_ghost_ship:
            print(f"{total_scroll_count} Slot MCS Found: STAT: {added_stat_value}, WA: {added_att_value}")
        else:
            test_slot_scenario = total_scroll_count

            for i in range(1, 91):
                test_slot_scenario -= 1
                test_slot_stat = added_stat_value - (test_slot_scenario * scroll_stat_value)
                test_slot_att = added_att_value - (test_slot_scenario * scroll_att_value)
                if test_slot_stat <= (9 * i) and test_slot_att <= (9 * i):
                    print(f"{i} Slot MCS Found: STAT: {test_slot_stat}, WA: {test_slot_att}")
                    break

        print("\nAlright Calcs all done.\n")
        print("------------------------------------------\n")
        break


if __name__ == '__main__':
    main()

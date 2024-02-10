import add_movies, update_movies, update_movie_all_fields, read_movies, delete_movies

def from_report_return_to_main_app_menu_file():
    with open("PYTHON\\PYTHON PROJECT\\FILMFLIX\\app_menu_options.txt") as from_report_return_movies_file:
        from_report_return_menu_options = from_report_return_movies_file.read()
    return from_report_return_menu_options

def menu_select():
    choice = 0
    choices_list = ["1", "2", "3", "4", "5", "6", "7"]

    menu_options = from_report_return_to_main_app_menu_file()

    while choice not in choices_list:

        print(menu_options)

        choice = input("Please choose an option from the list above: ")

        if choice not in choices_list:
            
            print(f"{choice} is not on the list. Please try again.")
    return choice

subprogram = True

while subprogram:

    main_menu = menu_select()

    match main_menu:
        case "1":
            add_movies.add_movie()
        case "2":
            update_movies.update_movie()
        case "3":
            update_movie_all_fields.update_movie_all_fields()
        case "4":
            read_movies.read_movies()
        case "5":
            delete_movies.delete_movie()
        # case "6":
        #     subprogram = True
        #     while subprogram:
        #         print("Accessed value 6")
        #         report_main_menu.report_menu_file()
        #         subprogram = False
        case "7":
            subprogram = False
print("Thank you for using FilmFlix. Goodbye :)")
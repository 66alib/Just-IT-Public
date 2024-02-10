import display_all_movies, add_movies, update_movies, update_movie_all_fields, delete_movies, report_all_movies, report_genre, report_released, report_rating

def app_menu_file():
    with open("PYTHON\\PYTHON PROJECT\\FILMFLIX\\app_menu_options.txt") as movies_file:
        menu_options = movies_file.read()
    return menu_options

def menu_select():
    choice = 0
    choices_list = ["1", "2", "3", "4", "5", "6", "7"]

    menu_options = app_menu_file()

    while choice not in choices_list:

        print(menu_options)

        choice = input("Please choose an option from the list above: ")

        if choice not in choices_list:
            
            print(f"{choice} is not on the list. Please try again.")
    return choice

main_program = True

while main_program:

    main_menu = menu_select()

    match main_menu:
        case "1":
            add_movies.add_movie()
        case "2":
            update_movies.update_movie()
        case "3":
            update_movie_all_fields.update_movie_all_fields()
        case "4":
            display_all_movies.read_movies()
        case "5":
            delete_movies.delete_movie()
        case "6":
            def nested_report_menu():

                option = 0
                nested_option_list = ["1", "2", "3", "4", "5", "6"]

                while option not in nested_option_list:

                    print(                        
                        """
                        Filter Menu
                        ~~~~~~~~~~~~~~~~~~~~~
                        ---------------------------------------------
                        1. Display details of all films
                        2. Display films based on a genre
                        3. Display films based on release year
                        4. Display films based on rating
                        5. Return back to the Main Menu
                        6. Exit
                        ---------------------------------------------
                        """
                    )
                    
                    option = input("Enter an option from the menu above: ")

                    if option not in nested_option_list:

                        print(f"{option} is not a valid choice! Please try again.")
                return option  

            subprogram = True

            while subprogram:

                sub_menu = nested_report_menu()

                if sub_menu == "1":
                    report_all_movies.report_all_movies()
                elif sub_menu == "2":
                    report_genre.report_movies_genre()
                elif sub_menu == "3":
                    report_released.report_movies_released()
                elif sub_menu == "4":
                    report_rating.report_movies_rating()
                elif sub_menu == "5":
                    subprogram = False
                else: 
                    subprogram = False
                    main_program = False  
                    print("Thank you for using FilmFlix. Goodbye :)")   
        case "7":
            main_program = False
            print("Thank you for using FilmFlix. Goodbye :)")








total_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0

film_name = input()

while film_name != "Finish":

    free_spaces = int(input())
    ticket_type = 0

    loops = 0
    kids_tickets_m = 0
    student_tickets_m = 0
    standard_tickets_m = 0

    while ticket_type != "End" and loops != free_spaces:

        ticket_type = input()
        loops += 1

        if ticket_type == "standard":
            standard_tickets += 1
            standard_tickets_m += 1
        elif ticket_type == "student":
            student_tickets += 1
            student_tickets_m += 1
        elif ticket_type == "kid":
            kids_tickets += 1
            kids_tickets_m += 1

    total_tickets_for_current_movie = standard_tickets_m + kids_tickets_m + student_tickets_m
    total_tickets += total_tickets_for_current_movie
    fullness = total_tickets_for_current_movie / free_spaces * 100

    print(f"{film_name} - {fullness:.2f}% full.")

    film_name = input()


print(f"Total tickets: {total_tickets}\n"
      f"{student_tickets/total_tickets*100:.2f}% student tickets.\n"
      f"{standard_tickets/total_tickets*100:.2f}% standard tickets.\n"
      f"{kids_tickets/total_tickets*100:.2f}% kids tickets.")

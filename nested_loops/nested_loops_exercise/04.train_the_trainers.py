
number_of_judges = int(input())

presentation_assessment = 0
final_assessment = 0
loops = 0
presentation_name = input()


while presentation_name != "Finish":

    for i in range(number_of_judges):
        loops +=1
        mark = float(input())
        presentation_assessment += mark
        final_assessment += mark


    print(f"{presentation_name} - {presentation_assessment / number_of_judges:.2f}.")
    presentation_assessment = 0
    presentation_name = input()

print(f"Student's final assessment is {final_assessment / loops:.2f}.")

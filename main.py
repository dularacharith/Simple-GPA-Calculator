from gpa import get_gpa
def main():
    grades = []
    credits= []
    print("\n\t---------GPA CALCULATOR--------------\n")
    while True:
        try:
            how_many_grades = int(input("\nHow many grades to calculate: "))
            if how_many_grades:
                for i in range(how_many_grades):
                    while True:
                        try:
                            grade = str(input(f"\nEnter {i+1} Grade: ")).strip().upper()
                            credit = int(input(f"Enter Credits for {grade}: "))
                            if grade and grade in ["A+", "A", "A-","B+","B","B-","C+","C","C-","D+","D","E","F","FA"] and credit:
                                grades.append(grade)
                                credits.append(credit)
                                break
                            else:
                                print("\nInvalid Value!")
                        except ValueError:
                            print("\nEnter a valid value!")   
                get_gpa(grades,credits)
                break
            else:
                print("\nEnter a valid value!")
        except ValueError:
            print("\nEnter a valid value!")           
main()



    
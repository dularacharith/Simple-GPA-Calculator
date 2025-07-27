def get_grade_point(grade_list,credits_list):
    total_credits = 0
    total_grades = 0
    for grade,credit in zip(grade_list,credits_list):
        if grade == "A+":
            grade_point=4.0           
        elif grade == "A":
            grade_point=4.0            
        elif grade == "A-":
            grade_point=3.7            
        elif grade == "B+":
            grade_point=3.3           
        elif grade == "B":
            grade_point=3.0           
        elif grade == "B-":
            grade_point=2.7            
        elif grade == "C+":
            grade_point=2.3           
        elif grade == "C":
            grade_point=2.0            
        elif grade == "C-":
            grade_point=1.7           
        elif grade == "D+":
            grade_point=1.3         
        elif grade == "D":
            grade_point=1.0
        elif grade == "E":
            grade_point=0.0            
        else:
            pass
        total_grades += grade_point * credit
        total_credits += credit 
    return total_grades,total_credits

def get_gpa(grade_list,credit_list):
    total_grades,total_credits = get_grade_point(grade_list,credit_list)
    gpa = total_grades/total_credits
    print(f"\nYour GPA: {gpa}")

    







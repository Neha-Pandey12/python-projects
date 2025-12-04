from typing import List

def input_mark(subject_no:int)->int:
    while True:
        try:
            m=int(input(f"enter marks for subject{subject_no} (0-100:)").strip())
            if 0<=m<=100:
                return m
            print("please enter a number between 0 and 100.")
        except ValueError:
            print("invalid input-enter an integer.")

def letter_grade(percentage:float)->str:
    if percentage>=80:
        return "A"
    else:
        if percentage>=70:
            return "B"
        else:
            if percentage >=60:
                return "C"
            else:
                if percentage>=50:
                    return "D"
                else:
                    return "E"

def make_report(name:str,marks:List[int],filename:str)->None:
    total=sum(marks)
    percentage=total/len(marks)
    grade=letter_grade(percentage)
    distinction=all(m>75 for m in marks)

    lines=[
        f"Student Name : {name}",
        f"Marks        : "+" ,".join(str(m) for m in marks),
        f"Total Marks  : {total}",
        f"Percentage   : {percentage:2f}%",
        f"Grade        : {grade}",
        f"Distinction  : {'Yes' if distinction else 'No'}"
    ]

    print("\n--- Student Report ---")
    for line in lines:
        print(line)
    print("----------------------\n")

    with open (filename,"w",encoding="utf-8")as f:
        f.write("\n".join(lines))
    print(f"Report saved to {filename}")

def main():
    print("School Grading System (5 subjects)\n")
    name=input("Enter student name:").strip()or "Unknown Student"
    marks=[input_mark(i) for i in range(1,6)]
    filename=f"report_{name.replace('','_')}.txt"
    make_report(name,marks,filename)

if __name__=="__main__":
    main()


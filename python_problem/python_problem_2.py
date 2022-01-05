class Student:
    student_name_list = []
    student_number = 0
    grading_number = 0

    def __init__(self, name, mid_score, final_score):
        self.name = name
        self.mid = mid_score
        self.final = final_score
        self.aver = (mid_score + final_score)/2
    
    def append_Student(self, name):
        self.student_name_list.append(name)

#exception
class empty_Student(Exception):
    def __init__(self):
        super().__init__("No Stduent Data")

class exist_Name(Exception):
    def __init__(self):
        super().__init__("Already exist name!")

class all_Grading(Exception):
    def __init__(self):
        super().__init__("All Student have already received grades")

class not_all_Grading(Exception):
    def __init__(self):
        super().__init__("There is student who didn't get grades")

class not_exist_Name(Exception):
    def __init__(self):
        super().__init__("Not exist name!")

##############  menu 1
#매개변수가 필요한지 판단 후 코딩할 것) :
#사전에 학생 정보 저장하는 코딩 
def Menu1(name, mid_score, final_score):
    try:
        if name in Student.student_name_list:
            raise exist_Name
    except Exception as e:
        print(e)
    else:
        globals()[name] = Student(name, int(mid_score), int(final_score))
        globals()[name].append_Student(name)
        Student.student_number += 1


##############  menu 2
#매개변수가 필요한지 판단 후 코딩할 것) :
    #학점 부여 하는 코딩
def Menu2():
    for name in Student.student_name_list:
        if hasattr(globals()[name], 'grade'):
            continue
        else:
            if globals()[name].aver >= 90:
                globals()[name].grade = "A"
            elif globals()[name].aver >= 80:
                globals()[name].grade = "B"
            elif globals()[name].aver >= 70:
                globals()[name].grade = "C"
            else:
                globals()[name].grade = "D"
                
        Student.grading_number += 1
    print("Grading to all students")
##############  menu 3
#매개변수가 필요한지 판단 후 코딩할 것) :
    #출력 코딩
def Menu3():
    print("--------------------------------")
    print("name\t mid\t final\t grade")
    print("--------------------------------")
    for key in Student.student_name_list:
        print("{}\t {}\t {}\t {}".format(globals()[key].name, globals()[key].mid, globals()[key].final, globals()[key].grade))
##############  menu 4
#매개변수가 필요한지 판단 후 코딩할 것):
    #학생 정보 삭제하는 코딩
def Menu4(name):
    if hasattr(globals()[name], 'grade'):
        Student.grading_number -= 1
    Student.student_name_list.remove(name)
    Student.student_number -= 1

    print("{} student information is deleted".format(name))


#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출 
        try: 
            name, mid_score, final_score = input("Enter name, mid-score, final-score: ").split()
        
        except ValueError:
            print("Num of data is not 3")
        
        except inputError as e:
            print(e)
        
        else:
            Menu1(name, mid_score, final_score)

    elif choice == "2":
        # 예외사항 처리(저장된 학생 정보의 유무)
        # 예외사항이 아닌 경우 2번 함수 호출
        # "Grading to all students." 출력
        try:
            if Student.student_name_list.__len__() == 0:
                raise empty_Student
            
            elif Student.student_number == Student.grading_number:
                raise all_Grading
                

        except Exception as e:
            print(e)

        else:
            Menu2()


    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출
        try:
            if Student.student_name_list.__len__() == 0:
                raise empty_Student
                
            elif Student.student_number != Student.grading_number:
                raise not_all_Grading
        
        except Exception as e:
            print(e)
        
        else:
            Menu3()
        

    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        try:
            if Student.student_name_list.__len__() == 0:
                raise empty_Student
            else:
                inputName = input("Enter the name to delete: ")

                if inputName in Student.student_name_list:
                    Menu4(inputName)
                else:
                    raise not_exist_Name
        
        except Exception as e:
            print(e)

    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료
        print("Exit program")
        break

    else :
        #"Wrong number. Choose again." 출력
        print("Wrong number, Choose again.")
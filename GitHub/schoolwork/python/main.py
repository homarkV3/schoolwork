from courselist import CourseList
from course import Course

def main():
    term = CourseList()
    with open("data.txt","r") as data:
        for line in data:
            tempClass = line.split(",")
            newCourse = Course(tempClass[0], tempClass[1], tempClass[2], tempClass[3])
            term.insert(newCourse)

    return term
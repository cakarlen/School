//
//  schedule.hpp
//  Proj3
//
//  Created by Chase Karlen on 10/29/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#ifndef schedule_h
#define schedule_h

#include <iostream>
#include <iomanip>
using namespace std;

const int MAX_COURSES = 10;

class schedule {
public:
    schedule();
    
    int addCourse(string course);
    int dropCourse(string course);
    void print();
    
    int getNumCourses();
    string getStudentId();
    string getCourseId(int index);
    
    void setStudentId(string new_student_id);
//    void setCourseID(string new_course_id);
private:
    int num_courses;
    string student_id;
    string course_id[MAX_COURSES];
};

#endif /* schedule_hpp */

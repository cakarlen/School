//
//  schedule.cpp
//  Proj3
//
//  Created by Chase Karlen on 10/29/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#include "schedule.h"

schedule::schedule() {
    num_courses = 0;
    student_id = "";
}

void schedule::print() {
    cout << setw(5) << left << student_id << " " << setw(2) << right << num_courses << " ";
    for (int i = 0; i < num_courses; i++) {
        cout << course_id[i] << " ";
    }
    cout << endl;
}

int schedule::addCourse(string course) {
    if (num_courses < MAX_COURSES) {
        course_id[num_courses] = course;
        num_courses++;
        
        return 0;
    } else {
        return 1;
    }
}

int schedule::dropCourse(string course) {
    for (int i = 0; i < num_courses; i++) {
        if (course_id[i] == course) {
            num_courses--;
            
            for (int j = i; j < num_courses; j++) {
                course_id[j] = course_id[j + 1];
            }
            
            return 0;
        }
    }
    
    return -1;
}

string schedule::getStudentId() {
    return student_id;
}

int schedule::getNumCourses() {
    return num_courses;
}

string schedule::getCourseId(int index) {
    if (index < num_courses) {
        return course_id[index];
    } else {
        return "";
    }
}

void schedule::setStudentId(string new_student_id) {
    student_id = new_student_id;
}

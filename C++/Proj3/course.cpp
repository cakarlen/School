//
//  course.cpp
//  Proj3
//
//  Created by Chase Karlen on 10/29/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#include "course.h"

course::course() {
    hours = 0;
    id = "", course_num = "", dept = "", title = "";
}

int course::getHours() {
    return hours;
}

string course::getID() {
    return id;
}

string course::getCourseNum() {
    return course_num;
}

string course::getDept() {
    return dept;
}

string course::getTitle() {
    return title;
}

void course::setHours(int new_hours) {
    if (new_hours < 0) {
        new_hours = 0;
    }
    
    hours = new_hours;
}

void course::setID(string new_id) {
    id = new_id;
}

void course::setCourseNum(string new_course_num) {
    course_num = new_course_num;
}

void course::setDept(string new_dept) {
    dept = new_dept;
}

void course::setTitle(string new_title) {
    title = new_title;
}

void course::print() {
    cout << setw(5) << left << id << " " << setw(4) << left << dept << " " << setw(4) << left << course_num << " " << setw(3) << right << hours << setw(20) << left << title << endl;
}

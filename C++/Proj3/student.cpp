//
//  student.cpp
//  Proj3
//
//  Created by Chase Karlen on 10/29/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#include "student.h"

student::student() {
    id = "", first_name = "", last_name = "";
    hours = 0;
}

void student::print() {
    cout << setw(5) << left << id << " " << setw(3) << right << hours << " " << setw(15) << left << last_name << " " << setw(15) << left << first_name << endl;
}

string student::getId() {
    return id;
}

string student::getFirstName() {
    return first_name;
}

string student::getLastName() {
    return last_name;
}

int student::getHours() {
    return hours;
}

void student::setID(string new_id) {
    id = new_id;
}

void student::setFirstName(string new_first) {
    first_name = new_first;
}

void student::setLastName(string new_last) {
    last_name = new_last;
}

void student::setHours(int new_hours) {
    hours = new_hours;
}

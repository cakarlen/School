//
//  studentList.hpp
//  Proj3
//
//  Created by Chase Karlen on 10/29/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#ifndef studentList_h
#define studentList_h

#include <iostream>
#include <fstream>
#include "student.h"
using namespace std;

const int MAX_STUDENTS = 50;

class studentList {
public:
    studentList();
    
    void read();
    void print();
    student search(string id);
    student search(int index);
private:
    student stu_list[MAX_STUDENTS];
    int num_students;
};

#endif /* studentList_h */

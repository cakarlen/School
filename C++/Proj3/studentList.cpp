//
//  studentList.cpp
//  Proj3
//
//  Created by Chase Karlen on 10/29/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#include "studentList.h"

studentList::studentList() {
    num_students = 0;
}

void studentList::read() {
    ifstream read_file;
    
    int hours;
    string id, first_name, last_name;
    string file_name = "stulist.txt";
    
    read_file.open(file_name);
    
    if (!read_file.fail()) {
        read_file >> num_students;
        
        for (int i = 0; i < num_students; i++) {
            read_file >> id >> last_name >> first_name >> hours;
            stu_list[i].setID(id);
            stu_list[i].setFirstName(first_name);
            stu_list[i].setLastName(last_name);
            stu_list[i].setHours(hours);
        }
        
        read_file.close();
    } else {
        cout << "Student list text file could not be opened!" << endl;
        return;
    }
}

void studentList::print() {
    cout << "================ STUDENT LIST (" << num_students << ") ====================" << endl;
    cout << "IDNUM HRS LAST            FIRST" << endl;
    cout << "----- --- --------------- ---------------" << endl;
    for (int i = 0; i < num_students; i++) {
        stu_list[i].print();
    }
    cout << endl;
    system("pause");
}

student studentList::search(string course) {
    student local_stud;
    for (int i = 0; i < num_students; i++) {
        if (stu_list[i].getId() == course) {
            return stu_list[i];
        }
    }
    
    return local_stud;
}

student studentList::search(int index) {
    student local_stud;
    for (int i = 0; i < num_students; i++) {
        if (index <= i) {
            return stu_list[i];
        }
    }
    
    return local_stud;
}

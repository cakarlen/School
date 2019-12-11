//
//  catalog.cpp
//  Proj3
//
//  Created by Chase Karlen on 10/29/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#include "catalog.h"

catalog::catalog() {
    num_classes = 0;
}

void catalog::print() {
    cout << "=============== COURSE CATALOG ================" << endl;
    cout << "ID    DEPT NUMB HRS TITLE" << endl;
    cout << "----- ---- ---- --- ------------------------------" << endl;
    for (int i = 0; i < num_classes; i++) {
        classes[i].print();
    }
    cout << "=========== # courses listed: " << num_classes << " =============" << endl << endl;
    system("pause");
}

void catalog::read() {
    ifstream read_file;
    
    int hours;
    string id, course_num, dept, title, sentinel;
    string file_name = "catalog.txt";
    
    read_file.open(file_name);
    
    sentinel = "";
    if (!read_file.fail()) {
        while (sentinel != "XXXXX") {
            read_file >> id >> dept >> course_num >> hours;
            sentinel = id;
            
            if (read_file.peek() == '\n') read_file.ignore();
            getline(read_file, title);
            if (id != "XXXXX") {
                classes[num_classes].setID(id);
                classes[num_classes].setDept(dept);
                classes[num_classes].setCourseNum(course_num);
                classes[num_classes].setHours(hours);
                classes[num_classes].setTitle(title);
                
                num_classes++;
            }
        }
    
        read_file.close();
    } else {
        cout << "Catalog text file could not be opened!" << endl;
        return;
    }
}

course catalog::getCourse(int course_index) {
    course local_course;
    for (int i = 0; i < num_classes; i++) {
        if (course_index <= i) {
            return classes[i];
        }
    }
    
    return local_course;
}

int catalog::search(string id) {
    for (int i = 0; i < num_classes; i++) {
        if (classes[i].getID() == id) {
            return i;
        }
    }
    
    return -1;
}

//
//  schedList.cpp
//  Proj3
//
//  Created by Chase Karlen on 10/29/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#include "schedList.h"

schedList::schedList() {
    num_sched = 0;
}

void schedList::read() {
    ifstream read_file;
    
    int num_stud_courses;
    string id, courses;
    string file_name = "schedList.txt";
    
    read_file.open(file_name);
    
    if (!read_file.fail()) {
        read_file >> num_sched;
        
        for (int i = 0; i < num_sched; i++) {
            read_file >> id >> num_stud_courses;
            
            if (num_stud_courses > 0) {
                for (int j = 0; j < num_stud_courses; j++) {
                    read_file >> courses;
                    sched[i].addCourse(courses);
                }
                
                sched[i].setStudentId(id);
            }
        }
        
        read_file.close();
    } else {
        cout << "Schedule list text file could not be opened!" << endl;
        return;
    }
}

int schedList::getNumSchedules() {
    return num_sched;
}

void schedList::print() {
    cout << "=============== ALL SCHEDULES (" << num_sched << ") =================" << endl;
    cout << "STUID #C COURSE IDS" << endl;
    cout << "----- -- ---------------------------------------------" << endl;
    for (int i = 0; i < num_sched; i++) {
        sched[i].print();
    }
    cout << endl;
    system("pause");
}

void schedList::write() {
    // Declare ofstream object
    ofstream write_file;
    string file_name = "schedList_1.txt";
    
    write_file.open(file_name);
    // If file does not fail to open
    if (!write_file.fail()) {
        // Write to file the num_orders with a newline
        write_file << num_sched << endl;
        // Loop num_orders to write out each order/order attribute
        for (int i = 0; i < num_sched; i++) {
            // Write out each basket's orderNumber, numItems, totalPrice, and custName
            write_file << sched[i].getStudentId() << " " << sched[i].getNumCourses() << " ";
            for (int j = 0; j < sched[i].getNumCourses(); j++) {
                write_file << sched[i].getCourseId(j) << " ";
            }
            write_file << endl;
        }
        // Close the write_file to save data
        write_file.close();
    }
}

void schedList::addSchedule(schedule single_sched) {
    bool is_found = false;
    
    for (int i = 0; i < num_sched; i++) {
        if (single_sched.getStudentId() == sched[i].getStudentId()) {
            sched[i] = single_sched;
            is_found = true;
        }
    }
    
    if (!is_found) {
        if (num_sched < MAX_SCHED) {
            sched[num_sched] = single_sched;
            num_sched++;
        } else {
            cout << "Schedule list is full, cannot add new schedule!" << endl;
        }
    }
}

schedule schedList::getSchedule(string student_id) {
    schedule local_sched;
    for (int i = 0; i < num_sched; i++) {
        if (sched[i].getStudentId() == student_id) {
            return sched[i];
        }
    }
    
    return local_sched;
}

schedule schedList::getSchedule(int index) {
    schedule local_sched;
    
    for (int i = 0; i < num_sched; i++) {
        if (index <= i) {
            return sched[i];
        }
    }
    
    return local_sched;
}

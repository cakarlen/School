//
//  schedList.hpp
//  Proj3
//
//  Created by Chase Karlen on 10/29/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#ifndef schedList_h
#define schedList_h

#include <iostream>
#include <fstream>
#include "schedule.h"

const int MAX_SCHED = 50;

class schedList {
public:
    schedList();
    
    void read();
    void print();
    void write();
    void addSchedule(schedule single_sched);
    
    schedule getSchedule(int index);
    schedule getSchedule(string student_id);
    int getNumSchedules();
private:
    schedule sched[MAX_SCHED];
    int num_sched;
};

#endif /* schedList_h */

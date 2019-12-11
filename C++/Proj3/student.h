//
//  student.hpp
//  Proj3
//
//  Created by Chase Karlen on 10/29/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#ifndef student_h
#define student_h

#include <iostream>
#include <iomanip>
using namespace std;

class student {
public:
    student();
    
    void print();
    string getId();
    string getFirstName();
    string getLastName();
    int getHours();
    
    void setID(string new_id);
    void setFirstName(string new_first);
    void setLastName(string new_last);
    void setHours(int new_hours);
private:
    string id, first_name, last_name;
    int hours;
};

#endif /* student_hpp */

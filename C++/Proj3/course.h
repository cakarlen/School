//
//  course.hpp
//  Proj3
//
//  Created by Chase Karlen on 10/29/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#ifndef course_h
#define course_h

#include <iostream>
#include <iomanip>
using namespace std;

class course {
public:
    course();
    
    int getHours();
    string getID();
    string getCourseNum();
    string getDept();
    string getTitle();
    
    void setHours(int new_hours);
    void setID(string new_id);
    void setCourseNum(string new_course_num);
    void setDept(string new_dept);
    void setTitle(string new_title);
    
    void print();
private:
    int hours;
    string id, course_num, dept, title;
};

#endif /* course_hpp */

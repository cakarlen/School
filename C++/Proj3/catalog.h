//
//  catalog.hpp
//  Proj3
//
//  Created by Chase Karlen on 10/29/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#ifndef catalog_h
#define catalog_h

#include <iostream>
#include <fstream>
#include <iomanip>
#include "course.h"
using namespace std;

const int MAX_CLASSES = 50;

class catalog {
public:
    catalog();
    
    void read();
    void print();
    course getCourse(int course_index);
    int search(string id);
private:
    course classes[MAX_CLASSES];
    int num_classes;
};


#endif /* catalog_hpp */

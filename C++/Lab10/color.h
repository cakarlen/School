//
//  color.h
//  Lab10
//
//  Created by Chase Karlen on 11/18/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#ifndef color_h
#define color_h

#include <iostream>
using namespace std;

class color {
    // friend stuff
   friend color operator + (color a, color b);
   friend color operator - (color a, color b);
    
public:
    // init
    color();
    
    // getters
    int getRedColor();
    int getGreenColor();
    int getBlueColor();
    
    // setters
    void set(int r, int g, int b);
    
    // print
    void print();
private:
    int red_color, green_color, blue_color;
};

// non-friend
color operator * (int num, color a);
color operator / (color a, int num);

#endif /* color_h */

//
//  color.cpp
//  Lab10
//
//  Created by Chase Karlen on 11/18/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#include "color.h"

color::color() {
    red_color = 0;
    green_color = 0;
    blue_color = 0;
}

int color::getRedColor() {
    return red_color;
}

int color::getGreenColor() {
    return green_color;
}

int color::getBlueColor() {
    return blue_color;
}

void color::set(int r, int b, int g) {
    if (r < 0) {
        red_color = 0;
    } else if (r > 255) {
        red_color = 255;
    } else {
        red_color = r;
    }
    
    if (b < 0) {
        blue_color = 0;
    } else if (b > 255) {
        blue_color = 255;
    } else {
        blue_color = b;
    }
    
    if (g < 0) {
        green_color = 0;
    } else if (g > 255) {
        green_color = 255;
    } else {
        green_color = g;
    }
}

void color::print() {
    cout << "R:" << red_color << "  B:" << blue_color << "  G:" << green_color << endl;
}

color operator + (color a, color b) {
    color local_color;
    
    int red = a.red_color + b.red_color;
    int blue = a.blue_color + b.blue_color;
    int green = a.green_color + b.green_color;
    local_color.set(red, blue, green);
    
    return local_color;
}

color operator - (color a, color b) {
    color local_color;
    
    int red = a.red_color - b.red_color;
    int blue = a.blue_color - b.blue_color;
    int green = a.green_color - b.green_color;
    local_color.set(red, blue, green);
    
    return local_color;
}

color operator * (int num, color a) {
    color local_color;
    
    int red = num * a.getRedColor();
    int blue = num * a.getBlueColor();
    int green = num * a.getGreenColor();
    local_color.set(red, blue, green);
    
    return local_color;
}

color operator / (color a, int num) {
    color local_color;
    
    if (num > 0) {
        int red = a.getRedColor() / num;
        int blue = a.getBlueColor() / num;
        int green = a.getGreenColor() / num;
        local_color.set(red, blue, green);
    } else {
        local_color.set(0, 0, 0);
    }
    
    return local_color;
}

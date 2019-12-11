//
//  menu.hpp
//  Proj3
//
//  Created by Chase Karlen on 10/29/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#ifndef menu_h
#define menu_h

#include <iostream>
#include <string>
using namespace std;

const int MAX_OPTIONS = 10;

class menu {
public:
    menu();
    
    char doMenu();
    void addOption(char input, string message);
    void setTitle(string title_message);
    void setErrorMessage(string message);
    bool validOption(char input);
private:
    string title, error_message;
    string menu_options[MAX_OPTIONS];
    char char_options[MAX_OPTIONS];
    int num_options;
};

#endif /* menu_hpp */

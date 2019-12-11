//
//  menu.cpp
//  Proj3
//
//  Created by Chase Karlen on 10/29/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#include "menu.h"

menu::menu() {
    num_options = 0;
    title = "", error_message = "";
}

bool menu::validOption(char input) {
    for (int i = 0; i < num_options; i++) {
        if (char_options[i] == input) {
            return true;
        }
    }
    
    return false;
}

char menu::doMenu() {
    cout << title << endl;
    for (int i = 0; i < num_options; i++) {
        cout << char_options[i] << ". " << menu_options[i] << endl;
    }
    
    string menu_input;
    char option = '\0';
    
    cout << "Enter option: ";
    if (cin.peek() == '\n') cin.ignore();
    getline(cin, menu_input);
    option = toupper(menu_input[0]);
    
    while (!validOption(option)) {
        cout << error_message << endl;
        cout << "Enter option: ";
        if (cin.peek() == '\n') cin.ignore();
        getline(cin, menu_input);
        option = toupper(menu_input[0]);
    }
    
    return option;
}

void menu::addOption(char input, string message) {
    if (num_options < MAX_OPTIONS) {
        char_options[num_options] = input;
        menu_options[num_options] = message;
        
        num_options++;
    } else {
        cout << "There is no room for more options!" << endl;
    }
}

void menu::setTitle(string title_message) {
    title = title_message;
}

void menu::setErrorMessage(string message) {
    error_message = message;
}

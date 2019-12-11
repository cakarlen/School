//
//  main.cpp
//  Lab8
//
//  Created by Chase Karlen on 10/31/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#include "student.h"

student::student() {
    stu_name = "";
    num_scores = 0;
    
    for (int i = 0; i < MAX_SCORES; i++) {
        scores[i] = 0;
    }
    cout << "Constructed!" << endl;
}

void student::setName(string new_name) {
    stu_name = new_name;
}

string student::getName() {
    return stu_name;
}

int student::getNumScores() {
    return num_scores;
}

void student::addScore(int new_score) {
    if (num_scores < MAX_SCORES) {
        scores[num_scores] = new_score;
        num_scores++;
    } else {
        cout << "MAX SCORES exceeded!" << endl;
    }
}

double student::getAvg() {
    double temp = 0.0;
    double result = 0.0;
    
    if (num_scores == 0) {
        return 0.0;
    } else {
        for (int i = 0; i < num_scores; i++) {
            temp += scores[i];
        }
        
        result = temp / num_scores;
    }
    
    return result;
}

void student::print() {
    cout << "Name=" << stu_name << " " << "Avg=" << getAvg() << " " << "#scores=" << num_scores << " scores=";
    for (int i = 0; i < num_scores; i++) {
        cout << scores[i] << " ";
    }
    cout << endl;
}

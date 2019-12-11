//
//  student.h
//  Lab8
//
//  Created by Chase Karlen on 10/31/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#ifndef student_h
#define student_h

#include <iostream>
using namespace std;

const int MAX_SCORES = 10;

class student {
public:
    student();
    
    void setName(string new_name);
    
    void print();
    void addScore(int new_score);
    string getName();
    int getNumScores();
    double getAvg();
private:
    string stu_name;
    int num_scores;
    int scores[MAX_SCORES];
};

#endif /* student_h */

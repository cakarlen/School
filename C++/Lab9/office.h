//
//  office.hpp
//  Lab9
//
//  Created by Chase Karlen on 11/6/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#ifndef office_h
#define office_h

#include <iostream>
#include <string>
#include <iomanip>
#include "candidate.h"
using namespace std;

const int MAX_CAND = 7;

class office {
public:
    office();
    
    void setOfficeName(string new_name);
    string getOfficeName();
    int getNumCandidates();
    
    void doVote();
    void print();
    void printReport();
    void addCandidate(int num_ballot, string party_name, string name);
    candidate getCandidate(int index);
private:
    string office_name;
    candidate cand[MAX_CAND];
    int num_cand;
};

#endif /* office_hpp */

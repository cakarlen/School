//
//  office.cpp
//  Lab9
//
//  Created by Chase Karlen on 11/6/19.
//  Copyright © 2019 Chase Karlen. All rights reserved.
//

#include "office.h"

office::office() {
    num_cand = 0;
    office_name = "";
}

void office::setOfficeName(string new_name) {
    office_name = new_name;
}

string office::getOfficeName() {
    return office_name;
}

int office::getNumCandidates() {
    return num_cand;
}

void office::addCandidate(int num_ballot, string party_name, string name) {
    if (num_ballot + 1 < MAX_CAND) {
        cand[num_cand].setBallotNum(num_ballot);
        cand[num_cand].setParty(party_name);
        cand[num_cand].setName(name);
        num_cand++;
    } else {
        cout << "office::addCandidate: max candidates exceeded" << endl;
    }
}

candidate office::getCandidate(int index) {
    candidate local_cand;
    for (int i = 0; i < num_cand; i++) {
        if (index <= i) {
            return cand[i];
        }
    }
    
    return local_cand;
}

void office::doVote() {
    int user_input;
    
    cout << "Enter ballot number: ";
    cin >> user_input;
    
    while (user_input < 1 || user_input > num_cand) {
        cout << "Invalid selection, try again!" << endl;
        cout << "Enter ballot number: ";
        cin >> user_input;
    }
    
    cand[user_input - 1].addVote();
    cout << "You voted for " << cand[user_input - 1].getName() << ". Thank you!" << endl;
    print();
    
}

void office::print() {
    cout << "Election for " << office_name << endl;
    for (int i = 0; i < num_cand; i++) {
        cand[i].print();
    }
}

void office::printReport() {
    cout << "Report of election for " << office_name << endl;
    for (int i = 0; i < num_cand; i++) {
        cout << setw(2) << right << "  " << cand[i].getBallotNum() << "  " << setw(3) << left << cand[i].getParty() << "  " << setw(15) << left << cand[i].getName() << setw(4) << right << cand[i].getVotes() << endl;
    }
}

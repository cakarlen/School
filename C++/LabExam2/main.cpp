//-------------------------------------------------------
//                CS 215 - Lab Exam 2 – A
//                   Chase Karlen
//-------------------------------------------------------

#include <iostream>
using namespace std;

/* BEGIN SCORE */

class score {
public:
    // init
    score();
    
    // getters
    int getPointsMade();
    int getPointsPossible();
    
    // setters
    void setPointsMade(int points);
    void setPointsPossible(int points);
    
    // methods
    double perc();
    void print();
private:
    int pointsMade, pointsPossible;
};

score::score() {
    pointsPossible = 1;
    pointsMade = 0;
}

double score::perc() {
    return (double(pointsMade) / double(pointsPossible)) * 100;
}

int score::getPointsMade() {
    return pointsMade;
}

int score::getPointsPossible() {
    return pointsPossible;
}

void score::setPointsMade(int points) {
    pointsMade = points;
}

void score::setPointsPossible(int points) {
    pointsPossible = points;
}

void score::print() {
    cout << pointsMade << " / " << pointsPossible << " (" << perc() << "%)" << endl;
}


/* BEGIN STUDENT */
const int MAX_SCORES = 5;

class student {
public:
    // init
    student();
    
    // setters
    void addScore(int made, int possible);
    
    // getters
    score getScore(int index);
    int getNumScores();
    
    // methods
    void print();
    double overall();
    score search(int possiblePoints);
private:
    score scoreArr[MAX_SCORES];
    int numScores;
};

student::student() {
    numScores = 0;
}

void student::addScore(int made, int possible) {
    if (numScores < MAX_SCORES) {
        scoreArr[numScores].setPointsMade(made);
        scoreArr[numScores].setPointsPossible(possible);
        numScores++;
    } else {
        cout << "Max exceeded!" << endl;
    }
}

score student::getScore(int index) {
    score local_score;
    
    for (int i = 0; i < numScores; i++) {
        if (index == i) {
            return scoreArr[i];
        }
    }
    
    return local_score;
}


int student::getNumScores() {
    return numScores;
}

double student::overall() {
    double sumMade = 0, sumPossible = 0;
    
    if (numScores > 0) {
        for (int i = 0; i < numScores; i++) {
            sumMade += scoreArr[i].getPointsMade();
            sumPossible += scoreArr[i].getPointsPossible();
        }
        
        return (sumMade / sumPossible) * 100;
    } else {
        return 100.0;
    }
}

score student::search(int possiblePoints) {
    score local_score;
    for (int i = 0; i < numScores; i++) {
        if (scoreArr[i].getPointsPossible() == possiblePoints) {
            return scoreArr[i];
        }
    }
    
    return local_score;
}

void student::print() {
    for (int i = 0; i < numScores; i++) {
        scoreArr[i].print();
    }
}

bool operator < (score one, score two) {
    if (one.perc() < two.perc()) {
        return true;
    } else {
        return false;
    }
}

score operator * (int num, score one) {
    one.setPointsMade(num * one.getPointsMade());
    one.setPointsPossible(num * one.getPointsPossible());

    return one;
}


/* BEGIN MAIN */
int main() {
    cout << "\nQuestion 1:--------------\n";
    // test the score class
    score s;
    s.print();
    s.setPointsMade(20); s.setPointsPossible(25);
    s.print();
    cout << "Made=" << s.getPointsMade() << " Possible=" << s.getPointsPossible() <<  " Perc=" << s.perc() << endl;
    
    // test the student class
    student x;
    cout << "#scores = " << x.getNumScores() << endl;
    x.addScore(40, 50);
    x.addScore(75, 100);
    x.addScore(10, 20);
    x.addScore(40, 40);
    x.addScore(10, 15);
    x.addScore(30, 35); // should print "Max Exceeded"
    cout << "#scores = " << x.getNumScores() << endl;
    x.print();
    s = x.getScore(-1); s.print();
    s = x.getScore(6);  s.print();
    s = x.getScore(3);  s.print();
    system("pause");

    cout << "\nQuestion 2:-------------\n";
    cout << "Overall of x = " << x.overall() << endl;
    student y;    // 0 scores
    cout << "Overall of y = " << y.overall() << endl;
    system("pause");

    cout << "\nQuestion 3:-------------\n";
    s = x.search(100); cout << "search(100)= "; s.print();
    s = x.search(50);  cout << "search(50) = "; s.print();
    s = x.search(15);  cout << "search(15)= ";  s.print();
    s = x.search(200); cout << "search(200)= "; s.print(); // not found
    system("pause");

    cout << "\nQuestion 4:-------------\n";
    score s1, s2;
    s1.setPointsMade(20); s1.setPointsPossible(30); // % = 66.666
    s2.setPointsMade(40); s2.setPointsPossible(80); // % = 50.0
    if (s1 < s2) cout << "bad1\n";  else cout << "good1\n";
    if (s2 < s1) cout << "good2\n"; else cout << "bad2\n";
    s2.setPointsPossible(60); // % = 66.666, so now s1==s2
    if (s1 < s2) cout << "bad3\n";  else cout << "good3\n";
    s2 = 2 * s1; s2.print();
    system("pause");

    return 0;
}

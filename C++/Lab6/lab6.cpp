//--------------------------------------------------------------------
// CS215-401 LAB 6
//--------------------------------------------------------------------
// Author: Chase Karlen
// Date: 10-22-19
//--------------------------------------------------------------------

#include <iostream>
#include <iomanip>
using namespace std;

// a fraction structure
struct frac {
    int num; // numerator
    int den; // denominator
};

//-----------------------------------------------------------------------
//                              AskFraction
//-----------------------------------------------------------------------
frac AskFraction() {
    // Initialize local frac
    frac new_frac;
    
    // Get num/den for local frac
    cout << "Enter numerator:       ";
    cin >> new_frac.num;
    cout << "Enter denominator > 0: ";
    cin >> new_frac.den;
    
    // Input validation check on den
    while (new_frac.den < 1) {
        cout << "Enter denominator > 0: ";
        cin >> new_frac.den;
    }
    
    // Return local frac
    return new_frac;
}

//-----------------------------------------------------------------------
//                              DecimalValue
//-----------------------------------------------------------------------
double DecimalValue(frac frac_input) {
    double answer;
    // Divide num by den
    answer = double(frac_input.num) / double(frac_input.den);
    
    // Return double (answer)
    return answer;
}

//-----------------------------------------------------------------------
//                              PrintFraction
//-----------------------------------------------------------------------
void PrintFraction(frac frac_input) {
    // Print "header" for frac_input
    cout << setw(3) << frac_input.num << endl;
    cout << "----" << " = " << DecimalValue(frac_input) << endl;
    cout << setw(3) << frac_input.den << endl;
}

//-----------------------------------------------------------------------
//                              Multiply
//-----------------------------------------------------------------------
frac Multiply(frac frac_1, frac frac_2) {
    // Initialize local frac
    frac answer;
    
    // Perform calculations on frac parameters and put into local frac
    answer.num = frac_1.num * frac_2.num;
    answer.den = frac_1.den * frac_2.den;
    
    // Return local frac
    return answer;
}

//-----------------------------------------------------------------------
//                              Add
//-----------------------------------------------------------------------
frac Add(frac frac_1, frac frac_2) {
    // Initialize local frac
    frac answer;
    
    // If both frac parameter's den is the same
    if (frac_1.den == frac_2.den) {
        // Perform calculations on num since den is the same
        answer.num = frac_1.num + frac_2.num;
        answer.den = frac_1.den;
    }
    else {
        // Perform calculations to add both frac parameters
        answer.num = ((frac_1.num * frac_2.den) + (frac_1.den * frac_2.num));
        answer.den = frac_1.den * frac_2.den;
    }
    
    // Return local frac
    return answer;
}

//-----------------------------------------------------------------------
//                              Simplify
//-----------------------------------------------------------------------
void Simplify(frac& mod_frac) {
    // Count from frac parameter den down to 2
    for (int i = mod_frac.den; i >= 2; i--) {
        // If frac parameter num and den don't have a remainder
        if (mod_frac.num % i == 0 && mod_frac.den % i == 0) {
            // Divide each by i
            mod_frac.num /= i;
            mod_frac.den /= i;
        }
    }
    // Invoke PrintFraction with frac parameter
    PrintFraction(mod_frac);
}

//-----------------------------------------------------------------------
//                              main
//-----------------------------------------------------------------------
int main() {
    // Initialize local frac variables
    frac user_frac_1;
    frac user_frac_2;
    frac answer, multiply_answer;
    
    // Prompt user to populate 2 fractions
    cout << "FRACTION 1:" << endl;
    user_frac_1 = AskFraction();
    cout << endl << "FRACTION 2:" << endl;
    user_frac_2 = AskFraction();
    
    // Multiply fractions
    multiply_answer = Multiply(user_frac_1, user_frac_2);
    cout << "PRODUCT:" << endl;
    PrintFraction(multiply_answer);
    cout << endl;
    
    // Add fractions
    answer = Add(user_frac_1, user_frac_2);
    cout << "SUM:" << endl;
    PrintFraction(answer);
    cout << endl;
    
    // Simplify fractions
    cout << "PRODUCT SIMPLIFIED:" << endl;
    Simplify(multiply_answer);
    
    system("pause");
    return 0;
}

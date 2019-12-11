//--------------------------------------------------------------------
// CS215-401 LAB 5
//--------------------------------------------------------------------
// Author: Chase Karlen
// Date: 10-16-19
// Description: Append and edit text using a text file
//--------------------------------------------------------------------

#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

const int MAX_FRIENDS = 5;
struct afriend {
    string name;
    string phone;
    string email;
};

int main() {
    string file_name = "friends.txt";
    string name, phone, email, temp_name, temp_phone, temp_email, option_input;
    int friend_index, low_index = 0, high_index = 0;
    char option_char = '\0';
    
    ifstream read_file;
    ofstream write_file;
    
    afriend list[MAX_FRIENDS];
    int num_friends;
    
    read_file.open(file_name);
    
    if (!read_file.fail()) {
        read_file >> num_friends;
        
        for (int i = 0; i < num_friends; i++) {
            read_file >> name >> phone >> email;
            
            list[i].name = name;
            list[i].phone = phone;
            list[i].email = email;
        }
        read_file.close();
        
        while (option_char != 'X') {
            cout << "-------------------- Friend List ---------------------" << endl;
            cout << setw(3) << "Num " << setw(10) << left << "Name" << setw(13) << right << "Phone" << setw(13) << "Email" << endl;
            cout << setw(3) << "--- " << setw(10) << "----------------- " << "------------ " << "-------------------" << endl;
            for (int i = 0; i < num_friends; i++) {
                if (i > high_index) {
                    high_index = i;
                }
                
                cout << setw(3) << right << i << " " << setw(10) << left << list[i].name << setw(20) << right << list[i].phone << " " << setw(15) << left << list[i].email << endl;
            }
            cout << "------------------------------------------------------" << endl;
            
            cout << "Options: A=Add  E=Edit  X=Exit" << endl;
            cout << "Enter A, E, or X: ";
            cin >> option_input;
            option_char = toupper(option_input[0]);
            
            while (option_char != 'A' && option_char != 'E' && option_char != 'X') {
                cout << "Invalid entry! Try again!" << endl;
                cout << "Enter A, E, or X: ";
                cin >> option_input;
                option_char = toupper(option_input[0]);
            }
            
            switch (option_char) {
                case 'A':
                    if (num_friends < MAX_FRIENDS) {
                        cout << "Enter name:  ";
                        cin >> name;
                        cout << "Enter phone: ";
                        cin >> phone;
                        cout << "Enter email: ";
                        cin >> email;
                        
                        list[num_friends].name = name;
                        list[num_friends].phone = phone;
                        list[num_friends].email = email;
                        
                        num_friends++;
                    }
                    else {
                        cout << "Sorry, your friends list is full!" << endl;
                    }
                    
                    break;
                case 'E':
                    cout << "Enter num of friend to edit (" << low_index << "-" << high_index << "): ";
                    cin >> friend_index;
                    
                    while (friend_index < low_index || friend_index > high_index) {
                        cout << "Invalid entry! Try again!" << endl;
                        cout << "Enter num of friend to edit (" << low_index << "-" << high_index << "): ";
                        cin >> friend_index;
                    }
                    
                    for (int i = 0; i < num_friends; i++) {
                        if (i == friend_index) {
                            temp_name = list[i].name;
                            temp_phone = list[i].phone;
                            temp_email = list[i].email;
                            friend_index = i;
                        }
                    }
                    
                    cout << "Name: " << temp_name << endl;
                    cout << "Enter new name:  ";
                    cin >> name;
                    cout << "Phone: " << temp_phone << endl;
                    cout << "Enter new phone: ";
                    cin >> phone;
                    cout << "Email: " << temp_email << endl;
                    cout << "Enter new email: ";
                    cin >> email;
                    
                    list[friend_index].name = name;
                    list[friend_index].phone = phone;
                    list[friend_index].email = email;
                    
                    break;
                default:
                    break;
            }
            
            cout << endl;
        }
    }
    else {
        cout << "Could not open file!" << endl;
    }
    
    cout << "Thanks for using Friendbook!" << endl;
    system("pause");
    return 0;
}

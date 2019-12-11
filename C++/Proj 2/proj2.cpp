//-----------------------------------------------------------
// CS 215-401 – Project 2
//-----------------------------------------------------------
// Author: Chase Karlen
// Date: 10-18-2019
// Description: An application that allows customers to order items from an inventory of products
// Assistance: I received help from the following:
// StackOverflow.com - Help with semantics on adding orders to each basket
//-----------------------------------------------------------

#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
using namespace std;

const int READ_ERROR = -1;
const int MAX_INV_ITEMS = 10;
const int MAX_ORDER_ITEMS = 5;
const int MAX_ORDERS = 7;

// describes a single item in the inventory, and on an order
struct item {
    string prodCode;        // product code: length 12, no spaces
    string description;        // product description: max length 28, has spaces
    double price;            // price of the product, max 999.99
};

// describes a customer order or "basket"
struct order {
    long   orderNumber;        // unique order number for this order
    string custName;        // customer name
    double totalPrice;        // price of all items purchased
    item items[MAX_ORDER_ITEMS];    // list of items purchased
    int numItems;            // number of items purchased
};

//-----------------------------------------------------------
//                      readInventory
//-----------------------------------------------------------
void readInventory(item inv[], int& num_items, int& last_order_num) {
    ifstream f;
    string file_name = "inventory.txt";
    
    // open the inventory file
    f.open(file_name);
    if (f.fail()) {
        cout << "readFile:: error opening inventory.txt" << endl;
        num_items = READ_ERROR;
        return;
    }
    
    // read number of items from first line
    f >> num_items >> last_order_num;
    
    // for each item, read the data for the item
    for (int i = 0; i < num_items; i++) {
        f >> inv[i].prodCode >> inv[i].price;
        f.ignore(); // finished reading integer, getline() on string is next
        getline(f, inv[i].description);
    }
    f.close();
} // readInventory()

//-----------------------------------------------------------
//                      getMainOption
//-----------------------------------------------------------
char getMainOption() {
    // Needed prototype to use isValidOption
    bool isValidOption(char input, string validOptions);
    // Initialize local variables
    string menu_input;
    char menu_char;
    
    // Print headers
    cout << "+-----------------------------------------------+" << endl;
    cout << "|\t\tGOODPRODUCTS.COM\t\t|" << endl;
    cout << "|\t\tby Chase Karlen\t\t\t|" << endl;
    cout << "+-----------------------------------------------+" << endl;
    cout << "I - List our Inventory" << endl;
    cout << "O - Make an Order" << endl;
    cout << "L - List all Orders made" << endl;
    cout << "X - Exit" << endl;
    
    // Get user input with getline
    cout << "Enter an option: ";
    if (cin.peek() == '\n') cin.ignore();
    getline(cin, menu_input);
    menu_char = toupper(menu_input[0]);
    
    // Input validation check with isValidOption
    while (!isValidOption(menu_char, "IOLX")) {
        cout << "Invalid option, enter I, O, L or X!" << endl;
        cout << "Enter an option: ";
        if (cin.peek() == '\n') cin.ignore();
        getline(cin, menu_input);
        menu_char = toupper(menu_input[0]);
    }
    
    // Return a valid, upper-case character
    return menu_char;
}

//-----------------------------------------------------------
//                      isValidOption
//-----------------------------------------------------------
bool isValidOption(char input, string validOptions) {
    // Get length of valid char string
    int string_length = validOptions.length();
    
    // Loop through each character (index) in string
    for (int i = 0; i < string_length; i++) {
        // If indexed valid char in string is equal to user input
        if (validOptions[i] == input) {
            return true;
        }
    }
    
    // Return false by default
    return false;
}

//-----------------------------------------------------------
//                      displayList
//-----------------------------------------------------------
void displayList(item inv[], int num_items) {
    cout << fixed << setprecision(2);
    
    // Loop through num_items and display inventory attributes
    for (int i = 0; i < num_items; i++) {
        cout << setw(3) << right << i << "  ";
        cout << setw(12) << left << inv[i].prodCode << "  $";
        cout << setw(6) << right << inv[i].price << "  ";
        cout << setw(28) << left << inv[i].description << endl;
    }
}

//-----------------------------------------------------------
//                      displayInventory
//-----------------------------------------------------------
void displayInventory(item inv[], int num_items) {
    // Print headers
    cout << "+------------------------------------------------------+" << endl;
    cout << "|                        Products                      |" << endl;
    cout << "+------------------------------------------------------+" << endl;
    cout << " #   PRODUCT CODE   PRICE   PRODUCT DESCRIPTION " << endl;
    cout << "---  ------------  -------  ----------------------------" << endl;
    // Call displayList to display inventory items with their attributes
    displayList(inv, num_items);
    cout << "Number of items in inventory: " << num_items << endl;
}

//-----------------------------------------------------------
//                      displayOrder
//-----------------------------------------------------------
void displayOrder(order ord) {
    // Print header with a single order's attributes
    cout << "ORDER: " << ord.orderNumber << "\t" << ord.custName << endl;
    // Call displayList to display order
    displayList(ord.items, ord.numItems);
    cout << "Total:\t\t   $" << setw(6) << right << ord.totalPrice << endl;
}

//-----------------------------------------------------------
//                      startOrder
//-----------------------------------------------------------
void startOrder(order orders[], int& num_orders, int& last_order_num) {
    // Initialize local variables and increment last_order_num
    string cust_name;
    last_order_num++;
    
    // Get user input for customer name
    cout << "Order Number:        " << last_order_num << endl;
    cout << "Enter customer name: ";
    if (cin.peek() == '\n') cin.ignore();
    getline(cin, cust_name);
    
    // Initialize new basket in occordance with num_orders
    orders[num_orders].orderNumber = last_order_num;
    orders[num_orders].custName = cust_name;
    orders[num_orders].totalPrice = 0;
    orders[num_orders].numItems = 0;
    
    // Increment num_orders
    num_orders++;
}

//-----------------------------------------------------------
//                      orderItem
//-----------------------------------------------------------
bool orderItem(item inv[], order orders[], int num_items, int& num_orders) {
    // Initialize local variables
    int index_input;
    double price = 0;
    string item_desc, prod_code;
    
    // Get user input for item number to order
    cout << endl << "Enter item number (-1 to end): ";
    cin >> index_input;
    
    // Item number input validation check
    while (index_input < -1 || index_input >= num_items) {
        cout << "Invalid entry. Enter number -1 to " << num_items - 1 << endl;
        cout << "Enter item number (-1 to end): ";
        cin >> index_input;
    }
    
    // If index_input does not equal -1 (to quit order)
    if (!(index_input == -1)) {
        // If number of items in an order does not exceed the MAX_ORDER_ITEMS
        if (!(orders[num_orders - 1].numItems >= MAX_ORDER_ITEMS)) {
            // Save item attributes within inv in temp variables
            item_desc = inv[index_input].description;
            price = inv[index_input].price;
            prod_code = inv[index_input].prodCode;
            
            // Save new basket initialized in startOrder with the temp variables created
            orders[num_orders - 1].items[orders[num_orders - 1].numItems].description = item_desc;
            orders[num_orders - 1].items[orders[num_orders - 1].numItems].price = price;
            orders[num_orders - 1].items[orders[num_orders - 1].numItems].prodCode = prod_code;
            
            // Increment totalPrice within basket
            orders[num_orders - 1].totalPrice += orders[num_orders - 1].items[orders[num_orders - 1].numItems].price;
            // Print item description added
            cout << orders[num_orders - 1].items[orders[num_orders - 1].numItems].description << " added to your basket.";
            // Print current total
            cout << " Current total is $ " << orders[num_orders - 1].totalPrice << endl;
            
            // Increment numItems within basket
            orders[num_orders - 1].numItems++;
            // If MAX_ORDER_ITEMS has been exceeded
        }
        else {
            cout << "Sorry, the max number of items per order is " << MAX_ORDER_ITEMS << "!" << endl;
            return true;
        }
    }
    else {
        return true;
    }
    
    // Return false by default for loop to continue
    return false;
}

//-----------------------------------------------------------
//                      makeOrder
//-----------------------------------------------------------
void makeOrder(item inv[], order orders[], int& num_items, int& num_orders, int& last_order_num) {
    // If num_orders has exceeded MAX_ORDERS
    if (num_orders >= MAX_ORDERS) {
        cout << "Sorry, we can not take more orders today." << endl;
    }
    else {
        // Invoke each function needed to start/make/print orders
        startOrder(orders, num_orders, last_order_num);
        displayInventory(inv, num_items);
        while (!orderItem(inv, orders, num_items, num_orders));
        
        cout << "Thank you for your order!" << endl;
        displayOrder(orders[num_orders - 1]);
    }
    
    system("pause");
}

//-----------------------------------------------------------
//                      listOrders
//-----------------------------------------------------------
void listOrders(order orders[], int num_orders) {
    // Prototype for displayOrder
    void displayOrder(order ord);
    
    // Print headers
    cout << "+------------------------------------------------------+" << endl;
    cout << "|                        Orders                        |" << endl;
    cout << "+------------------------------------------------------+" << endl;
    // For each order, invoke displayOrder on it
    for (int i = 0; i < num_orders; i++) {
        displayOrder(orders[i]);
        cout << endl;
    }
    cout << "Total number of orders = " << num_orders << endl;
}

//-----------------------------------------------------------
//                      writeOrders
//-----------------------------------------------------------
void writeOrders(order orders[], int num_orders) {
    // Declare ofstream object
    ofstream write_file;
    string file_name = "orders.txt";
    
    write_file.open(file_name);
    // If file does not fail to open
    if (!write_file.fail()) {
        // Write to file the num_orders with a newline
        write_file << num_orders << endl;
        // Loop num_orders to write out each order/order attribute
        for (int i = 0; i < num_orders; i++) {
            // Write out each basket's orderNumber, numItems, totalPrice, and custName
            write_file << orders[i].orderNumber << " " << orders[i].numItems << " " <<
            orders[i].totalPrice << " " << orders[i].custName << endl;
            // Nested for loop to loop through the individual order
            for (int j = 0; j < orders[i].numItems; j++) {
                // Write out an individual order's prodCode, price, and description
                write_file << orders[i].items[j].prodCode << " " <<
                orders[i].items[j].price << " " <<
                orders[i].items[j].description << endl;
            }
        }
        // Close the write_file to save data
        write_file.close();
    }
}

//-----------------------------------------------------------
//                          main
//-----------------------------------------------------------
int main() {
    // Prototype for makeOrder
    void makeOrder(item inv[], order orders[], int& num_items, int& num_orders, int& last_order_num);
    
    // Initialize local variables
    int last_order_num, num_items, num_orders = 0;
    char menu_choice;
    
    // Declare partial arrays for item and order
    item inv[MAX_INV_ITEMS];
    order orders[MAX_ORDERS];
    
    // Invoke readInventory to generate num_items and last_order_num
    readInventory(inv, num_items, last_order_num);
    
    // Do/while loop to loop through main menu options until user enters 'X'
    do {
        // Invoke getMainOption to get a valid, upper-case char (option)
        menu_choice = getMainOption();
        
        // Switch/case based on menu_choice and invoke respective function based on input
        switch (menu_choice) {
            case 'I':
                cout << endl;
                displayInventory(inv, num_items);
                cout << endl;
                break;
            case 'L':
                listOrders(orders, num_orders);
                cout << endl;
                break;
            case 'O':
                makeOrder(inv, orders, num_items, num_orders, last_order_num);
                cout << endl;
                break;
            case 'X':
                writeOrders(orders, num_orders);
                cout << endl;
                break;
        }
    } while (menu_choice != 'X');
    
    system("pause");
    return 0;
}


#include <iostream>
#include "LList.h"

//----------------------------------------------------
//                constructor & destructor
//----------------------------------------------------
LList::LList() {
    head = NULL;
    cout << "LList: constructed!\n";
}

LList::~LList() {
    if (head != NULL) {
        delete head;
    }
    cout << "LList: destructed!\n";
}

//----------------------------------------------------
//                         search
//----------------------------------------------------
// Given: key to search for
// Returns: pointer to a node in the list found to have
//          the given search key, or NULL for not found
//----------------------------------------------------
node * LList::search(int srchKey) {
    node *n = head;
    
    while (n != NULL) {
        if (n->key == srchKey) {
            return n;
        }
        n = n->next;
    }
    
    return NULL;
} // search()

//----------------------------------------------------
//                   findNode
//----------------------------------------------------
// Given: a key to search for
// Searches for a node with the given key, and if
// found, invokes the print() method in the found node.
// Otherwise, prints "not found"
//----------------------------------------------------
void LList::findNode(int srchkey) {
    node *n = head;
    
    while (n != NULL) {
        if (n->key == srchkey) {
            n->print();
            return;
        }
        n = n->next;
    }
    
    cout << "Not found!" << endl;
} // findNode()

//----------------------------------------------------
//                    getb4
//----------------------------------------------------
// Given: a pointer to a node in the list
// Returns: a pointer to the node in the list BEFORE
//               the one pointed to by r, OR
//          NULL when r is the head or not found in
//               the list
//----------------------------------------------------
node * LList::getb4(node * r) {
    node *b4 = new node;
    b4 = head;
    
    if (r == head) {
        return NULL;
    }
    
    if (b4 == NULL) {
        return NULL;
    }
    
    while (b4 != NULL) {
        if (b4->next == r) {
            return b4;
        }
        
        b4 = b4->next;
    }
    
    return NULL;
} // getb4()

//----------------------------------------------------
//                       insert
//----------------------------------------------------
// Given: key and data for a new node
// Allocates/populates a new node
// When a node with the same key already exists:
//     the current/old node is replaced by the new one
//     and the old one is placed on the new one's
//     duplicate list (it's NEXT should be set to NULL,
//     since it is no longer "in the list")
// Otherwise, the new node is prepended to the head
//     of the list.
//----------------------------------------------------
void LList::insert(int k, string d) {
    node * newNode = new node;
    newNode->key = k;
    newNode->data = d;
    
    if (head == NULL) {
        newNode->next = NULL;
        head = newNode;
        
        return;
    }
    
    node *foundSearch = search(k);
    if (foundSearch) {
        node *findB4 = getb4(foundSearch);
        
        if (newNode->key == head->key) {
            // Put old head node in newNode dup
            newNode->dup = head;
            // Null old head node next
            newNode->dup->next = NULL;
            // Init head to newNode
            head = newNode;
        } else {
//            newNode->next = findB4->next;
            findB4->next->next = NULL;
            newNode->dup = findB4->next;
            findB4->next = newNode;
        }
    } else {
        // Didn't find
        newNode->next = head;
        head = newNode;
    }
} // insert()

//----------------------------------------------------
//                       remove
//----------------------------------------------------
// Given: a pointer to a node in the list to be removed
//        BUT NOT DELETED/DESTROYED
// Returns: TRUE - when the node was successfully removed
//          FALSE - when the given node is NULL or the node
//                  is not actually in the list.
// Simply removes the node from the linked list.
// (including setting the NEXT pointer in the node to NULL)
//----------------------------------------------------
bool LList::remove(node * r) {
    if (r == head) {
        head = head->next;
    } else {
        node * b4 = head;
        
        while (b4->next != r) {
            b4 = b4->next;
        }
        b4->next = r->next;
        return true;
    }
    
    r->next = NULL;
    return false;
} // remove()

//----------------------------------------------------
//                       drop
//----------------------------------------------------
// Given: key of a node to drop
// Returns: TRUE when a node was found and deleted
//          FALSE when a node with the given key not found,
//                or the remove() fails.
// Searches for a node in the list with the given key:
// When found, removes and deletes the node
//----------------------------------------------------
bool LList::drop(int k) {
    node *print = head;
    
    while (print != NULL) {
        if (print->key == k) {
            delete print;
            return remove(print);
        }
        
        print = print->next;
    }
    
    return false;
} // drop()

//----------------------------------------------------
//                        max
//----------------------------------------------------
// Returns: a pointer to the node with the highest key
//          or NULL when there list is empty.
node * LList::max() {
    int max = 0;
    
    node * p = head;
    while (p != NULL) {
        if (max < p->key) {
            max = p->key;
        }
        
        if (max == p->key) {
            return p;
        }
        
        p = p->next;
    }
    
    return NULL;
} // max()

//----------------------------------------------------
//                       sort
//----------------------------------------------------
// Sorts the list in ascending order by key values
void LList::sort() {

} // sort()

  //----------------------------------------------------
  //                    print
  //----------------------------------------------------
  // prints each node in the list, or EMPTY when there
  // are no nodes to print
  //----------------------------------------------------
void LList::print() {
    if (head == NULL)
        cout << "EMPTY\n\n";
    else {
        node * p;
        p = head;
        while (p != NULL) {
            p->print();
            p = p->next;
        }
        cout << endl;
    }
} // print()

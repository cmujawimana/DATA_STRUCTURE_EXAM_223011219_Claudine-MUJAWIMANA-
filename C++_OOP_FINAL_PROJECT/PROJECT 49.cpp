#include <iostream>        
#include <cstring>         
using namespace std;       
struct MenuItem {
    char name[30];         
    float price;           
};

class Order {
public:
    MenuItem** items;      
    int nItems;            
    Order(MenuItem** items, int nItems) : items(items), nItems(nItems) {}
    virtual float totalCost() = 0;
    virtual ~Order() {}
};
class TableOrder : public Order {
public:
    TableOrder(MenuItem** items, int nItems) : Order(items, nItems) {}
    float totalCost() override {
        float total = 0;
        for (int i = 0; i < nItems; ++i)          
            total += (*(items + i))->price;        
        return total + 200;                         
    }
};
class DeliveryOrder : public Order {
public:
    DeliveryOrder(MenuItem** items, int nItems) : Order(items, nItems) {}
    float totalCost() override {
        float total = 0;
        for (int i = 0; i < nItems; ++i)            
            total += (*(items + i))->price;        
        return total + 500;                          
    }
};

class OrderSystem {
    Order** orders;         
    int count;              
public:
    
    OrderSystem() : orders(nullptr), count(0) {}
    void addOrder(Order* o) {
        Order** newOrders = new Order*[count + 1];        
        for (int i = 0; i < count; ++i)                   
            newOrders[i] = orders[i];
        newOrders[count] = o;                             
        delete[] orders;                                  
        orders = newOrders;                               
        count++;                                          
    }
    // Remove an order by index
    void removeOrder(int index) {
        if (index < 0 || index >= count) {               
            cout << "Invalid order index.\n";
            return;
        }
        Order** newOrders = new Order*[count - 1];        
        for (int i = 0, j = 0; i < count; ++i) {
            if (i != index)                               
                newOrders[j++] = orders[i];               
        }
        delete orders[index];                             
        delete[] orders;                                  
        orders = newOrders;                               
        count--;                                          
    }

    void showTotals() {
        for (int i = 0; i < count; ++i) {
            cout << "Order " << i << " total: rwf"<<" "
                 << orders[i]->totalCost() << endl;       
        }
    }
    ~OrderSystem() {
        for (int i = 0; i < count; ++i)
            delete orders[i];                             
        delete[] orders;                                  
    }
};
void displayMenu(MenuItem menu[], int size) {
    cout << "MENU:\n";
    for (int i = 0; i < size; ++i)                        
        cout << i << ". " << menu[i].name << " - rwf"<<" "
             << menu[i].price << endl;                    
}
int main() {
    MenuItem menu[5] = {
        {"Burger", 1000},
        {"Pizza", 500},
        {"Juice", 1500},
        {"Fries", 3000},
        {"Salad", 1200}
    };
    int menuSize = 5;                                     
    OrderSystem system;                                     
    int choice;                                            
    while (true) {
        cout << "\n1. Add Table Order\n2. Add Delivery Order\n3. Remove Order\n4. Show All Totals\n5. Exit\nChoice: ";
        cin >> choice;                                     
        if (choice == 1 || choice == 2) {
            int nItems;
            displayMenu(menu, menuSize);                  
            cout << "How many items in the order? ";
            cin >> nItems;
            MenuItem** selectedItems = new MenuItem*[nItems]; 
            for (int i = 0; i < nItems; ++i) {
                int itemIndex;
                cout << "Enter menu index for item " << i + 1 << ": ";
                cin >> itemIndex;
                if (itemIndex >= 0 && itemIndex < menuSize) 
                    selectedItems[i] = &menu[itemIndex];    
                else {
                    cout << "Invalid index. Using item 0 by default.\n";
                    selectedItems[i] = &menu[0];            
                }
            }
            if (choice == 1)
                system.addOrder(new TableOrder(selectedItems, nItems));
            else
                system.addOrder(new DeliveryOrder(selectedItems, nItems));
        } else if (choice == 3) {
            int index;
            cout << "Enter order index to remove: ";
            cin >> index;
            system.removeOrder(index);                     
        } else if (choice == 4) {
            system.showTotals();                           
        } else if (choice == 5) {
            break;                                        
        } else {
            cout << "Invalid choice. Try again.\n";       
        }
    }
    return 0;                                              
}
 

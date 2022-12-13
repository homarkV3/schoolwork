// groceries_template.cpp: Stores Orders in a list.

#include <fstream>
#include <sstream>
#include <iostream>
#include <list>
#include <fstream>
#include <algorithm>
#include <stdexcept>
#include <string>
#include <vector>
#include "split.h"
using namespace std;

//////////////////
// Customer code /
//////////////////
struct Customer {
    int cust_id;
    string name;
    string street;
    string city;
    string state;
    string zip;
    string phone;
    string email;
    Customer(int id, const string& name, const string& street, const string& city,
             const string& state, const string& zip, const string& phone, const string& email)
        : name(name), street(street), city(city), state(state), zip(zip), phone(phone), email(email) 
    {
        cust_id = id;
    }
    string print_detail() const {
        return "Customer ID #" + to_string(cust_id) + ":\n" +
        name + ", ph. " + phone + ", email: " + email + "\n" +
        street + "\n" + city + ", " + state + " " + zip + "\n";
    }
};
vector<Customer> customers;

void read_customers(const string& fname) {
    ifstream orderf(fname);
    string line;
    string delimiter = ",";
    size_t line_last = 0;
    size_t line_next = 0;  
    int id;
    string name;
    string street;
    string city;
    string state;
    string zip;
    string phone;
    string email;
    int lastint = 0;
    while (getline(orderf, line)){
        vector<string> line1 = split(line, ',');
        id = stoi(line1[0]);
        name = line1[1];
        street = line1[2];
        city = line1[3];
        state = line1[4];
        zip = line1[5];
        phone = line1[6];
        email = line1[7];
        customers.push_back(Customer(id, name, street, city, state, zip, phone, email));
    }
}

int find_cust_idx(int cust_id) {
    for (int i = 0; i < customers.size(); ++i)
        if (cust_id == customers[i].cust_id)
            return i;
    throw runtime_error("Customer not found");
}

//////////////
// Item code /
//////////////
struct Item {
    int item_id;
    string description;
    double price;
    Item(int id, const string& desc, double pric) : description(desc) {
        item_id = id;
        price = pric;
    }
};
vector<Item> items;

void read_items(const string& fname) {
    ifstream orderf(fname);
    string line;
    string delimiter = ",";
    while (getline(orderf, line))
    {
        size_t line_last = 0;
        size_t line_next = 0;  
        int id;
        string desc;
        double pric;
        int lastint = 0;
        
        while ((line_next = line.find(delimiter, line_last)) != string::npos){
            if (lastint == 0){
                id = stoi(line.substr(line_last, line_next-line_last));
            }
            else if (lastint == 1){
                desc = line.substr(line_last, line_next-line_last);
            }
            line_last = line_next + 1;
            lastint += 1;
        }
        pric = stof(line.substr(line_last));
        items.push_back(Item(id, desc, pric));
    }
}


int find_item_idx(int item_id) {
    for (int i = 0; i < items.size(); ++i)
        if (item_id == items[i].item_id)
            return i;
    throw runtime_error("Item not found");
}

class LineItem {
    int item_id;
    int qty;
    friend class Order;
public:
    LineItem(int id, int q) {
        item_id = id;
        qty = q;
    }
    double sub_total() const {
        int idx = find_item_idx(item_id);
        return items[idx].price * qty;
    }
    friend bool operator<(const LineItem& item1, const LineItem& item2) {
        return item1.item_id < item2.item_id;
    }
};

/////////////////
// Payment code /
/////////////////
class Payment {
    double amount;
    friend class Order;
public:
    Payment();
    // virtual ~Payment() = default;
    virtual string print_detail() const = 0;
};

class Credit : public Payment {
    string card_number;
    string date;
public:
    Credit(string card_number, string date){
        this->date = date;
        this->card_number = card_number;
    }
    string print_detail() const {
        return "Paid by Credit card " + card_number + ", exp. " + date + "\n";
    }
};

class Paypal : public Payment {
    string paypal_id;
public:
    Paypal(string paypal_id){
        this->paypal_id = paypal_id;
    }
    string print_detail() const {
        return "Paid by Paypal ID: " + paypal_id + "\n";
    }
};

class WireTransfer : public Payment {
    string bank_id;
    string account_id;
public:
    WireTransfer(string bank_id, string account_id){
        this->bank_id = bank_id;
        this->account_id = account_id;
    }
    string print_detail() const {
        return "Paid by Wire transfer from Bank ID " + bank_id + ", Account# " + account_id + "\n";
    }
};

///////////////
// Order code /
///////////////
class Order {
    int order_id;
    string order_date;
    int cust_id;
    vector<LineItem> line_items;
    Payment* payment;
public:
    Order(int id, const string& date, int c_id, const vector<LineItem>& items, Payment* p) 
    : order_date(date), line_items(items) {
        order_id = id;
        cust_id = c_id;
        payment = p;
        sort(line_items.begin(), line_items.end());
    }
    ~Order() {
        delete payment;
    }
    double total() const {
        double total_amount = 0;
        for(int i=0; i < line_items.size(); i++){
            total_amount += line_items.at(i).sub_total();
        }
        return total_amount;
    }
    string print_order() const {
            int cust_index = find_cust_idx(cust_id);
            string cust_string = customers.at(cust_index).print_detail();
            stringstream ss;
            ss << fixed << setprecision(2) << "===========================" <<
                   "\nOrder #" << to_string(order_id) << ", Date: " << order_date <<
                   "\nAmount: $" << total() << ", " << payment->print_detail() <<
                   "\n" << cust_string << "\nOrder Detail:";// this is four lines long
            for(int i = 0; i < line_items.size(); i++) {
                int item_id = line_items.at(i).item_id;
                int item_index = find_item_idx(item_id);
                string item_name = items.at(item_index).description;
                double item_price = items.at(item_index).price;

                ss << "\n    Item " << item_id << ": \"" << item_name + "\", " << line_items.at(i).qty << " @ " << item_price;
            }
            ss << endl;
            return ss.str();
        }
};
list<Order> orders;

void read_orders(const string& fname) {
    ifstream orderf(fname);
    string line;
    string delimiter = ",";
    string temp = "";
    int cust_id;
    int order_id;
    string date;
    string token;
    int iline = 1;
    vector<LineItem> line_items;
        // Create line item vector
    while (getline(orderf, line)) {
        // split line
        size_t line_last = 0;
        size_t line_next = 0;    
        int lastint = 0;
        // Extract cust_id, order_id, and date
        if (iline == 1){
            iline = 2 ;
            while ((line_next = line.find(delimiter, line_last)) != string::npos){
                if (lastint == 0)
                    cust_id = stoi(line.substr(line_last, line_next-line_last));
                else if (lastint == 1)
                    order_id = stoi(line.substr(line_last, line_next-line_last));
                else if (lastint == 2)
                    date = line.substr(line_last, line_next-line_last);
                else {     // Create line item vector
                    temp = line.substr(line_last, line_next-line_last);
                    size_t item_last = 0;
                    size_t item_next = 0;
                    string delimiter2 = "-";
                    int id = 0;
                    int q = 0;
                    int tracker = 0;
                    while ((item_next = temp.find(delimiter2, item_last)) != string::npos){
                        if (tracker == 0)
                            id = stoi(temp.substr(item_last, item_next-item_last));
                        item_last = item_next + 1;
                        tracker += 1;
                        }
                    line_items.push_back(LineItem(id, stoi(temp.substr(item_last))));
                    }
                    line_last = line_next + 1;
                    lastint += 1;
                }
            temp = line.substr(line_last);
            size_t item_last = 0;
            size_t item_next = 0;
            string delimiter2 = "-";
            int id = 0;
            while ((item_next = temp.find(delimiter2, item_last)) != string::npos){
                id = stoi(temp.substr(item_last, item_next-item_last));
                item_last = item_next + 1;
                line_items.push_back(LineItem(id, stoi(temp.substr(item_last))));
                }
            }
        // Read payment method (by reading/splitting next line in file)
        else if (iline == 2) {
            iline = 1;
        // Create concrete Payment object on heap (pmt)
            Payment* pmt;
            vector<string> line2 = split(line, ',');
            switch(line2.at(0).at(0)) {
                case '1': 
                    pmt = new Credit(line2.at(1), line2.at(2));
                    break;
                case '2': 
                    pmt = new Paypal(line2.at(1));
                    break;
                case '3':
                    pmt = new WireTransfer(line2.at(1), line2.at(2));
                    break;
                default:
                    cout << "unable to read orders.txt" << endl;
        }
        sort(line_items.begin(), line_items.end());
        orders.emplace_back(order_id, date, cust_id, line_items, pmt);
        line_items.clear();
        }
    }
}


int main() {
    read_customers("customers.txt");
    read_items("items.txt");
    read_orders("orders.txt");

    ofstream ofs("order_report.txt");
    for (const Order& order: orders)
        ofs << order.print_order() << endl;
}
#include<bits/stdc++.h>
using namespace std;

int main() {
    int year;
    cin >> year;
    while (true){
        if (year % 4 == 2) {
            break;
        }
        else {
            year++;
        }
    }
    cout << year << endl;
}
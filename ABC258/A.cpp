#include<bits/stdc++.h>
using namespace std;

int main() {
    int k;
    cin >> k;
    if (k >= 60 and k < 70){
        cout << "22:0" << (k-60) << endl;
    } 
    else if( k >= 70){
        cout << "22:" << (k-60) << endl;
    }
    else if( k >= 0 and k < 10){
        cout << "21:0" << k << endl;
    }
    else {
        cout << "21:" << k << endl;
    }
}
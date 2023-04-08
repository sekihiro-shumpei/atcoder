#include<bits/stdc++.h>
using namespace std;

int main() {
    int x;
    cin >> x;
    int ans = x;

    int syo, amari=0;

    while(x > 1){
        //syo = x / 10;
        
        amari += x % 10;
        x /= 10;


    }
    amari += x;
    //cout << amari << endl;
    if (ans % amari == 0) {
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }
}
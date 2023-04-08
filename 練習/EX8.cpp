#include<bits/stdc++.h>
using namespace std;

int main() {
    int p;
    cin >> p;

    
    if (p == 2) {
        string text;
        int price;
        cin >> text >> price;

        cout << text << "!" << endl;
    }

    int price, N;
    cin >> price >> N;

    //cout << N << endl;
    //cout << price << endl;
    cout << N * price << endl;
    
}
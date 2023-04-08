#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n;
    cin >> n;
    long long val = 1;
    for (int i = 0; i <= 60; i++){
        if (val > n){
            cout << i-1 << endl;
            break;
        }
        val *= 2;
    }
}
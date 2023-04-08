#include<bits/stdc++.h>
using namespace std;

int main() {
    int x, y, n;
    cin >> x >> y >> n;
    int price = 0, cnt = 0;
    if (x*3 > y && n >= 3){
        for(int i = 1; (i*3) <= n; i++){
            cnt += 3;
            price += y;
        }
        
        
        for(int i = 0; cnt < n; i++){
            cnt += 1;
            price += x;
        }
    } 
    else{
        for(int i = 0; i < n; i++){
            price += x;
        }
    }
    
    cout << price << endl;

}
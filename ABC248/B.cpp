#include<bits/stdc++.h>
using namespace std;

int main(){
    int a, b, k;
    int cnt = 0;
    cin >> a >> b >> k;

    if (a < b){
        while (a < b){
            a = a * k;
            cnt += 1;

        }
    }
    
    cout << cnt << endl;
}

03_handmade_01.txtのテストケースが通過できない。ワロス。
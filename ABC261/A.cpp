#include<bits/stdc++.h>
using namespace std;

int main() {
    int l1=0, r1 = 0, l2 = 0, r2 = 0, ans = 0;
    cin >> l1 >> r1 >> l2 >> r2;
    if (l1 <= l2 and r1 <= r2 and l2 <= r1) {
        ans = r1 - l2;
    } 
    else if (l2 <= l1 and r2 <= r1 and l1 <= r2) {
        ans = r2 - l1;
    }
    else if (l1 <= l2 and r2 <= r1){
        ans = r2 - l2;
    }
    else if (l2 <= l1 and r1 <= r2) {
        ans = r1 - l1;
    }
    else if (l1 == l2 and r1 == r2){
        ans = r1 - l1;
    }
    
    else {
        ans = 0;
    }
    cout << ans << endl;
}
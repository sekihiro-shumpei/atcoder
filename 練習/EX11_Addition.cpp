#include<bits/stdc++.h>
using namespace std;

int main() {
    int n, k, ans, ans_1 = 1, ans_2 = 1;
    cin >> n >> k;

    for (int i = 0; i < n; i++ ){
        ans_1 *= 2;
        ans_2 += k; 

        if (ans_1 < ans_2){
            ans = ans_1;
            ans_2 = ans_1;
        }
        else{
            ans = ans_2;
            ans_1 = ans_2;
        }
        
    }
    cout << ans << endl;
}
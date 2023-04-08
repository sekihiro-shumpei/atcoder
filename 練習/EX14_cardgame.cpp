#include<bits/stdc++.h>
using namespace std;

int main() {
    int n, ans = 0, alice_ans = 0, bob_ans = 0;
    


    cin >> n;
    vector<int> vec(n);
    for (int i = 0; i < n; i++){
        cin >> vec.at(i);
    }

    sort(vec.begin(), vec.end());
    reverse(vec.begin(), vec.end());

    for (int i = 0; i < n; i++){
        if (i % 2 == 0) {
            alice_ans += vec.at(i);
        } 
        else {
            bob_ans += vec.at(i);
        }
    }
    ans = alice_ans - bob_ans;

    cout << ans << endl;
  
}
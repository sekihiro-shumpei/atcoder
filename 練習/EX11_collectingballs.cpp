#include<bits/stdc++.h>
using namespace std;

int main() {
    int n, k, ans=0;
    cin >> n >> k;

    for (int i = 0; i < n; i++){
        int x_i;
        cin >> x_i;

        if (x_i < (k - x_i)){
            ans += 2 * x_i;
        }
        else{
            ans += 2 * (k - x_i);
        }
    }
    cout << ans << endl;

}
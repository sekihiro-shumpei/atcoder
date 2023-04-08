#include<bits/stdc++.h>
#include<algorithm>
using namespace std;



int base_k (string s, int k){
        int ans = 0;
        int pow = 1;
        reverse(s.begin(),s.end());
        for (int i = 0; i < s.size(); i++){
            ans += static_cast<int>(s.at(i) - '0') * pow;
            pow *= k;
        }
        return ans;
    }


int main(){
    int k;
    cin >> k;
    string a, b;
    cin >> a >> b;
    int ans = 0;

    ans = base_k(a,k) * base_k(b,k);
    //cout << base_k(a,k) << endl;

    cout << ans << endl;

    
}



できない。int 型を使っとるのが問題かも。
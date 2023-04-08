#include<bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> cnt(n,0);
    for (int i = 0; i < m; i++){
        int x, y;
        cin >> x >> y;
        cnt[x - 1]++, cnt[y-1]++;
    }
    
    for(int i = 0; i < n; i++){
        cout << cnt[i] <<endl;
    }
}
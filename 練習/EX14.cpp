#include<bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c;
    int min_ans, max_ans;
    cin >> a >> b >> c;

    min_ans = min(min(a,b),c);
    max_ans = max(max(a,b),c);

    cout << max_ans - min_ans << endl;


}
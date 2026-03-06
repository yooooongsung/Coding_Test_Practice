#include <bits/stdc++.h>
using namespace std;

int main() {
    int a,b,c;
    cin >> a >> b >> c;

    int time[100] = {0,};
    int start, end;

    for(int i = 0; i < 3; i++) {
        cin >> start >> end;
        for(int j = start; j < end; j++) {
            time[j]++;
        }
    }
    int res = 0;
    for(int k = 0; k < 100; k++) {
        if(time[k] == 3) res += (3*c);
        else if(time[k] == 2) res += (2*b);
        else if(time[k] == 1) res += a;
    }
    cout << res;
    return 0;
}
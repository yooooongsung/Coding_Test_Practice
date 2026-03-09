#include <bits/stdc++.h>
using namespace std;
int h, w;
string s;
int v[104][104];
int res[104][104];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> h >> w;

    for(int i = 0; i < h; i++) {
        cin >> s;
        for(int j = 0; j < w; j++) {
            v[i][j] = s[j];
        }
    }

    for(int i = 0; i < h; i++) {
        bool flag = false;
        int cnt = 0;

        for(int j = 0; j < w; j++) {
            if(v[i][j] == 'c') {
                res[i][j] = 0;
                flag = true;
                cnt = 0;
            }
            else if(v[i][j] == '.') {
                if(flag) {
                    cnt += 1;
                    res[i][j] = cnt;
                    continue;
                }
                res[i][j] = -1;
                
            }
        }
    }
    for(int i = 0; i < h; i++) {
        for(int j = 0; j < w; j++) {
            cout << res[i][j] << " ";
        }
        cout << "\n";
    }
    
    return 0;
}
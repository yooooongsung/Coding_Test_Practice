#include <bits/stdc++.h>
using namespace std;
int n, m, j, res;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    cin >> j;
    int head = 1;
    int rear = m;
    int apple, dist;
    for(int i = 0; i < j; i++) {
        cin >> apple;
        if(apple >= head && apple <= rear) continue;
        else if(apple > rear) {
            dist = apple - rear;
            res += dist;
            head += dist;
            rear = apple;
        }
        else if(apple < head) {
            dist = head - apple;
            res += dist;
            rear -= dist;
            head = apple;
            
        }
    }
    cout << res;
    
    return 0;
}
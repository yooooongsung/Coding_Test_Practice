    #include <bits/stdc++.h>
    using namespace std; 
    int k;
    string _min = "9999999999", _max = "";
    char arr[9];
    int visited[10];
    string s;
    void dfs(int num, int idx) {
        s.push_back(num + '0');
        visited[num] = 1;
        if(s.size() == k + 1) {
            if (s < _min) _min = s;
            if (s > _max) _max = s;
        }
        
        for(int j = 0; j <= 9; j++) {
            if(visited[j] == 0) {
                if(arr[idx] == '<') {
                    if(num < j) dfs(j, idx + 1);
                }
                else if(arr[idx] == '>') {
                    if(num > j) dfs(j, idx + 1);
                }
            }
        }

        s.pop_back();
        visited[num] = 0;
        return;
    }
    int main() {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL); cout.tie(NULL);
        cin >> k;
        for(int i = 0; i < k; i++) {
            cin >> arr[i];
        }
        for(int i = 0; i <= 9; i++) {
            // s = "";
            // memset(visited, 0, sizeof(visited));
            dfs(i, 0);
        }
        cout << _max << "\n" << _min;
        
        return 0;
    }
#include <bits/stdc++.h>

using namespace std;

int dfs(int i, int j, vector<vector<char>> container, int row, int col, vector<vector<int>> & visited) {
    int di[4] = {-1, 1, 0, 0};
    int dj[4] = {0, 0, -1, 1};
    for(int k = 0; k < 4; k++) {
        int ni = di[k] + i;
        int nj = dj[k] + j;
        if(0 <= ni && ni < row && 0 <= nj && nj < col && visited[ni][nj] == 0 && container[ni][nj] == '-') {
            visited[ni][nj] = 1;
            int res = dfs(ni, nj, container, row, col, visited);
            if(res == 1) return 1;
        }
        else if (ni < 0 || ni >= row || nj < 0 || nj >= col) return 1;
    }
    return 0;
}

int solution(vector<string> storage, vector<string> requests) {
    int answer = 0;
    int row = storage.size();
    int col = storage[0].size();
    vector<pair<int, int>> to_remove;
    vector<vector<char>> container (row, vector<char>(col, '.') );
    
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < col; j++) {
            container[i][j] = storage[i][j];
        }
    }
    
    for(int t = 0; t < requests.size(); t++) {
        if(requests[t].size() == 1) {
            for(int i = 0; i < row; i++) {
                for(int j = 0; j < col; j++) {
                    if(requests[t][0] == container[i][j]) {
                        if(i - 1 < 0 || i + 1 >= row || j - 1 < 0 || j + 1 >= col) to_remove.push_back({i, j});
                        else {
                            if(container[i-1][j] == '-' || container[i+1][j] == '-' || container[i][j-1] == '-' || container[i][j+1] == '-') {
                                vector<vector<int>> visited (row, vector<int> (col, 0));
                                int flag = dfs(i, j, container, row, col, visited);
                                if(flag == 1) to_remove.push_back({i, j});
                            }
                        }
                        
                    }
                }
            }
        }
        else {
            for(int i = 0; i < row; i++) {
                for(int j = 0; j < col; j++) {
                    if(requests[t][0] == container[i][j]) to_remove.push_back({i, j});
                }
            }
        }
        for(int a = 0; a < to_remove.size(); a++) {
            container[to_remove[a].first][to_remove[a].second] = '-';
        }
    }

    for(int i = 0; i < row; i++) {
        for(int j = 0; j < col; j++) {
            cout << container[i][j];
            if(isalpha(container[i][j])) answer += 1;
        }
        cout << endl;
    }
    return answer;
}
#include <bits/stdc++.h>

using namespace std;

int solution(vector<string> maps) {
    int answer = 0;
    int row = maps.size();
    int col = maps[0].size();
    int start[2] = {0, 0};
    int exit[2] = {0, 0};
    int lever[2] = {0, 0};
    vector<vector<char>> matrix (row, vector<char> (col, '.'));
    
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < col; j++) {
            matrix[i][j] = maps[i][j];
            if(matrix[i][j] == 'S') {
                start[0] = i;
                start[1] = j;
            }
            else if (matrix[i][j] == 'L') {
                lever[0] = i;
                lever[1] = j;
            }
            else if (matrix[i][j] == 'E') {
                exit[0] = i;
                exit[1] = j;
            }
        }
    }
    
    deque<pair<int, int>> q;
    q.push_back({start[0], start[1]});
    
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    
    vector<vector<int>> visited (row, vector<int> (col, 0));
    visited[start[0]][start[1]] = 1;
    bool flag = false;
    while(!q.empty() && !flag) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop_front();
        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(0 <= nx && nx < row && 0 <= ny && ny < col && visited[nx][ny] == 0) {
                if(matrix[nx][ny] == 'O' || matrix[nx][ny] == 'E') {
                    visited[nx][ny] = visited[x][y] + 1; // 여기서 바로 방문처리 하는게 맞나?
                    q.push_back({nx, ny});
                }
                else if(matrix[nx][ny] == 'L') {
                    visited[nx][ny] = visited[x][ny] + 1;
                    answer += visited[x][y];
                    flag = true;
                    break;
                }
            }
        }
    }
    if(flag == false) return -1;
    q.clear();
    q.push_back({lever[0], lever[1]});
    
    visited.assign(row, vector<int>(col, 0));
    visited[lever[0]][lever[1]] = 1;
    
    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop_front();
        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(0 <= nx && nx < row && 0 <= ny && ny < col && visited[nx][ny] == 0) {
                if(matrix[nx][ny] == 'X') continue;
                else if(matrix[nx][ny] == 'E') return answer += visited[x][y];
                visited[nx][ny] = visited[x][y] + 1;
                q.push_back({nx, ny});
            }
        }
    }
    
    return -1;
}
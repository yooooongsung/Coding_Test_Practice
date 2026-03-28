#include <bits/stdc++.h>
using namespace std; 
char chess[8][8];
int white, black;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    for(int i = 0; i < 8; i++) {
        for(int j = 0; j < 8; j++) {
            cin >> chess[i][j];
        }
    }
    for(int i = 0; i < 8; i++) {
        for(int j = 0; j < 8; j++) {
            if(chess[i][j] == 'P') white += 1;
            if(chess[i][j] == 'N') white += 3;
            if(chess[i][j] == 'B') white += 3;
            if(chess[i][j] == 'R') white += 5;
            if(chess[i][j] == 'Q') white += 9;
            if(chess[i][j] == 'p') black += 1;
            if(chess[i][j] == 'n') black += 3;
            if(chess[i][j] == 'b') black += 3;
            if(chess[i][j] == 'r') black += 5;
            if(chess[i][j] == 'q') black += 9;
        }
    }
    cout << white - black;
    return 0;
}
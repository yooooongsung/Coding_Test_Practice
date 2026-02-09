#include <bits/stdc++.h>
using namespace std;

vector<int> v = {1,2,3,4,5,6};
vector<bool> used(6, false);
vector<int> pick;

void dfs() {
    if (pick.size() == 2) {
        cout << pick[0] << " " << pick[1] << endl;
        return;
    }

    for (int i = 0; i < 6; i++) {
        if (!used[i]) {
            used[i] = true;
            pick.push_back(v[i]);
            dfs();
            pick.pop_back();
            used[i] = false;
        }
    }
}

int main() {
    dfs();
}



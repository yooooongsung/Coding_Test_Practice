#include <bits/stdc++.h>
using namespace std;
int n, res;
bool flag;
vector<char> st;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    for(int i = 0; i < n; i++) {
        string s;
        cin >> s;
        if(s.size() % 2 == 1) continue;

        st.push_back(s[0]); // A
        for(int j = 1; j < s.size(); j++) {
            // 알파벳의 짝이 맞는지
            // 교차하진 않은지, 즉 하나씩 나오는 경우라면 바로 탈락
            if(st.back() == s[j]) {
                st.pop_back(); // A
                continue;
            }
            st.push_back(s[j]); // A B
        }
        if(st.empty()) res++;
        else st.clear();
    }
    cout << res;
    
    return 0;
}
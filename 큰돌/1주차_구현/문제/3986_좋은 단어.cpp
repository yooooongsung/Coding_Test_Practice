#include <bits/stdc++.h>
using namespace std;
int n, res;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;

    for(int i = 0; i < n; i++) {
        string s;
        cin >> s;

        /* ver 1 */
        vector<char> st;
        for(char c : s) {
            if(!st.empty() && st.back() == c) st.pop_back();
            else st.push_back(c);
        }
        
        if(st.empty()) res++;

        /* ver 2
        st.push_back(s[0]); // A
        for(int j = 1; j < s.size(); j++) {
            if(st.back() == s[j]) {
                st.pop_back(); // A
                continue;
            }
            st.push_back(s[j]); // A B
        }
        if(st.empty()) res++;
        else st.clear(); */
    }
    cout << res;
    
    return 0;
}
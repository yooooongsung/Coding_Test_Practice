#include <bits/stdc++.h>
using namespace std; 
int n, k, temp, psum[100001], ret = -1e9;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	cin >> n >> k;
	for(int i = 0; i < n; i++) {
		cin >> psum[i];
	}
	for(int i = 0; i < k; i++) {
		temp += psum[i];
	}
	ret = max(ret, temp);
	for(int i = k; i < n; i++) {
		temp = temp + psum[i] - psum[i - k];
		ret = max(ret, temp);
	}
	cout << ret;
	
	return 0;
}

// #include<bits/stdc++.h> 
// using namespace std;  
// typedef long long ll;  
// int n, k, temp, psum[100001], ret = -10000000; 
// int main(){
// 	ios_base::sync_with_stdio(false);
// 	cin.tie(NULL);cout.tie(NULL);
    
// 	cin >> n >> k; 
// 	for(int i = 1; i <= n; i++){
// 		cin >> temp; psum[i] = psum[i - 1] + temp; 
// 	} 
// 	for(int i = k; i <= n; i++){
// 		ret = max(ret, psum[i] - psum[i - k]);
// 	}
// 	cout << ret << "\n";
//     return 0;
// }
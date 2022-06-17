#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, k, x, ml, d;
    vector<int> v;

    string fn1 = "270.txt";
    string fn2 = "27A.txt";
    string fn3 = "27B.txt";
    ifstream f(fn3);
    f >> n;
    f >> k;
    for(int i = 0; i < n; ++i) {
        f >> x;
        v.push_back(x);
    }
    f.close();

    ml = 0;
    for (int s = 0; s < n; ++s) {
        if (s% 10000 == 0)
             cout<<s<<" "<<n<<" "<<double(s)/n<<'\n';
        int sum = 0;
        for (int e = s; e < n && sum < k; ++e){
            sum += v[e];
            d = e-s+1;
            if (sum <= k && d > ml)
                ml = d;
        }
    }
    cout << ml;
    return 0;
}

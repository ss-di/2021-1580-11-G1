#include<bits/stdc++.h>

using namespace std;

int main() {
    
//    ifstream f("27_0.txt"); int vm = 96;  //32
//    ifstream f("27_A.txt"); int vm = 36;    //62885
    ifstream f("27_B.txt"); int vm = 36;
    int n;
    f >> n;
    vector<int> v1(n), v2(n);
    for (int i = 0; i < n; ++i)
        f >> v1[i] >> v2[i];
    f.close();

//    for (int i = 0; i < n; ++i)
//        cout << v1[i] << " " << v2[i] <<endl;

    
    long long st;
    long long min_st = -1;
    for (int p = 0; p < n; ++p){
        if (p % 100 == 0)
            cout << p << " " << n << " " << p/n*100 << '\n';
        st = 0;
        for (int i = 0; i < n; ++i)
            st += labs(v1[p] - v1[i]) * ((v2[i] + vm - 1) / vm);
        if (st < min_st || min_st == -1)
            min_st = st;
    }
    cout << min_st<<endl;
    cout << 1 * 2 + 3 * 1 + 5 * 1 + 6 * 1 + 8 * 2 <<endl;
    return 0;
}

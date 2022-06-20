#include<bits/stdc++.h>

using namespace std;

int main() {
    
//    ifstream f("27_0.txt"); int vm = 96;  //32
//    ifstream f("27_A.txt"); int vm = 36;    //62885
    ifstream f("27_B.txt"); int vm = 36; // 4 975 396 900 867
    int n;
    f >> n;
    vector<int> v1(n), v2(n), vp(n+1);
    for (int i = 0; i < n; ++i)
        f >> v1[i] >> v2[i];
    f.close();

//    for (int i = 0; i < n; ++i)
//        cout << v1[i] << " " << v2[i] <<endl;

    vp[0] = 0;
    for (int i = 0; i < n; ++i)
        vp[i+1] = vp[i] + ((v2[i] + vm - 1) / vm);

   long long st = 0;
   long long min_st = -1;
   int p = 0;
   for (int i = 0; i < n; ++i)
        st += labs(v1[p] - v1[i]) * ((v2[i] + vm - 1) / vm);
    min_st = st;

    for (int p = 1; p < n; ++p){
        int r = v1[p] - v1[p-1];
       // cout << r << " " << vp[p] << " " << vp[n] - vp[p] << endl;
        st += r * vp[p] - r * (vp[n] - vp[p]);
        //cout << st <<endl;
        if (st < min_st || min_st == -1)
            min_st = st;
    }
    cout << min_st<<endl;
    cout << 1 * 2 + 3 * 1 + 5 * 1 + 6 * 1 + 8 * 2 <<endl;
    return 0;
}

/*
6

1 2
2 3
5 1
7 1
8 1
10 2

2: 1*2 + 0*3 + 3*4 + 5*5 + 6*6 + 8*2
   3*2   3*3   3*4   3*5   3*6   3*2
5: 4*2 + 3*3 + 0*4 + 2*5 + 3*6 + 5*2


 * */

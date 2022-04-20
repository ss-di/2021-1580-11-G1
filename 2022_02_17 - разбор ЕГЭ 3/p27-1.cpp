#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main() {
    ifstream f;
    f.open("27-B.txt");
    int n;
    f >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
        f >> v[i];
    f.close();
    vector<int> pref(n+1);
    pref[0] = 0;
    for (int i = 0; i < n; i++)
        pref[i+1] = (pref[i] + v[i]) % 999;
    int cnt = 0;
    for (int i = 0; i < n; i++){
        if (i % 1000 == 0) cout << n << " " << i << endl;
        for (int j = i + 1; j < n + 1; j++)
            if ((pref[j] - pref[i]) % 999 == 0)
                cnt += 1;
    }

    cout << cnt;
    cin >> n;
    return 0;
}

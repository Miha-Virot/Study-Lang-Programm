#include <iostream>

using namespace std;

int main()
{
    int n = 0;
    string a;
    cin >> a;
    for (int i = 0; i < a.length(); i++)
    {
        if (a[i] == 'A' || a[i] == 'B' || a[i] == 'C' || a[i] == 'D' || a[i] == 'E' || a[i] == 'F' || a[i] == '0' || a[i] == '1' || a[i] == '2' || a[i] == '3' || a[i] == '4' || a[i] == '5' || a[i] == '6' || a[i] == '7' || a[i] == '8' || a[i] == '9') n++;
    }
    if (n == a.length()) cout << 1;
    else cout << 0;
    cout << endl;
    return 0;
}
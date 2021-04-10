#include <iostream>
using namespace std;

int main()
{
    int i;
    cin >> i;
    cout << i / 100 + i % 100 / 10 + i % 10 << endl;
}
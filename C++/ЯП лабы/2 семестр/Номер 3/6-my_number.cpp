#include <iostream>
using namespace std;

int main()
{
    int n = 5, a, b;
    float x = 0;
    for (int i = 1; i < n; i++)
    {
        a = rand() % 11;
        b = rand() % 11;
        x += a * b;
    }
    cout << x << endl;
    return 0;
}
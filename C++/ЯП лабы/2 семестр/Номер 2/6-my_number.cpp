#include <iostream>
#include <cmath>

using namespace std;

int main()
{

    int gs = 200;
    float pg = 0.8, f = 0.1, c = 0.5, l, t;
    while (c < 1.6)
    {
        l = (8 * gs) / (9 * c);
        t = l / (4 * sqrt(sqrt(gs * c)));
        cout << c << " | " << l << " | " << t << endl;
        c += 0.1;
    }
    return 0;
}
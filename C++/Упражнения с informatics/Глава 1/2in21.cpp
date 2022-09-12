#include <iostream>
using namespace std;

int main()
{
    int num, sqr, quad, result, quad2;
    cin >> num;
    sqr = num * num;     //num^2
    quad = sqr * sqr;    //num^4
    quad2 = quad * quad; //num^8
    result = quad2 * quad2 * quad * num;
    cout << result << endl;
}

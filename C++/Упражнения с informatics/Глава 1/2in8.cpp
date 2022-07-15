#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int num, sqr, quad, result;
    cin >> num;
    sqr = num * num;  //num^2
    quad = sqr * sqr; //num^4
    result = quad * quad;
    cout << result << endl;
}
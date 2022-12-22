#include <iostream>
#include <math.h>
using namespace std;

long long gcd(long long a, long long b)
{
	return b ? gcd(b, a % b) : a;

}
int main() {
	long long a, b, i, g, c = 0;
	cin >> a >> b;
	for (i = sqrt(a); i * i <= b; i++) {
		c += i * i > a ? 1 : 0;
	}
	if (c == 0) {
		cout << 0 << endl;
	}
	else {
		g = gcd(b - a, c);
		cout << c / g << "/" << (b - a) / g << endl;
	}
}
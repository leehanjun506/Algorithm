#include <string>
#include <vector>
#include <iostream>
// #include <algorithm>
using namespace std;

double solution(vector<int> arr) {
    int l = arr.size();
    double sum = 0;
    for (int i =0; i<l; i++){
        sum += arr[i];
    }
    double ans;
    ans = sum/l;
    return ans;
}
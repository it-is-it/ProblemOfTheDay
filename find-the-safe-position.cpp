// There are n people standing in a circle (numbered clockwise 1 to n) waiting to be executed. The counting begins at point 1 in the circle and proceeds around the circle in a fixed direction (clockwise). In each step, a certain number of people are skipped and the next person is executed. The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed), until only the last person remains, who is given freedom.
// Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle. The task is to choose the place in the initial circle so that you are the last one remaining and so survive.

#include <iostream>
using namespace std;

int safePos(int n, int k) {
    if (n == 1)
        return 1;
    else
        return (safePos(n - 1, k) + k-1) % n + 1;
}
// This function takes two arguments: n which is the total number of people in the circle and k which indicates that k-1 people are skipped and the kth person is killed. The function returns the position of the person who survives.

int main() {
    int n = 7;
    int k = 2;
    cout << "The chosen place is " << safePos(n, k);
    return 0;
}
// In this example, there are 7 people in the circle and every second person is killed (k=2). The function is called like this: safePos(7, 2) and it returns 7, meaning that the person in position 7 will be the last one remaining and will survive.

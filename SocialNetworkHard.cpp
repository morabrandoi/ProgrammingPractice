#include <iostream>
#include <unordered_set>
#include <queue>
using namespace std;

int main(){
    int n;
    int k;
    int curNum;
    unordered_set<int> membership;
    queue<int> running;
    cin >> n;
    cin >> k;

    for (int i = 0; i < n; i++){
        cin >> curNum;
        if (membership.find(curNum) != membership.end()) // if it is in hash
            continue;
        
        if (running.size() < k){
            running.push(curNum);
            membership.insert(curNum);
        }
        else{
            running.push(curNum);
            membership.erase(running.front());
            running.pop();
            membership.insert(curNum);
        }
    }

    unsigned int qSize = running.size();
    int rev[qSize];

    cout << running.size() << endl;

    for (int i = 0; i < qSize; i++){
        rev[i] = running.front();
        running.pop();
    }
    for (int a: rev){
        cout<< a << ' ';
    }

    
		
    return 0;
}

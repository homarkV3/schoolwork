#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<ctime>
#include<cstdlib>
#include<set>
#include<algorithm>
#include<random>
using namespace std;

int main() {
  // file read
    vector<string> words;
    ifstream file("words.txt");
    string key_word;
    while (file >> key_word) {
        words.__emplace_back(move(key_word));
    }
    // random number
    const int NWORDS = words.size();
    default_random_engine dre;
    uniform_int_distribution<int> di(0, NWORDS); 
    const int n  = di(dre);
    // key_word = words[n];
    key_word = "sodiums";

    const auto lengthcompare = [](const string& word1, const string& word2){
        if (word1.length() < word2.length()) {
            return true;
        } else if (word1.length() > word2.length()) {
            return false;
        }
        return word1 < word2;
        };
    set<string, decltype(lengthcompare)> subwords(lengthcompare);
    sort(key_word.begin(), key_word.end());
    do {
        for (int i = 3; i <= key_word.length(); ++i) {
            string newstr = key_word.substr(0, i);
            for (int i = 0; i < words.size(); i++){
                if (words[i] == newstr){
                    subwords.insert(newstr);
                }
            }
        }
    } while (next_permutation(key_word.begin(), key_word.end()));

    // output
    for (const string& subword : subwords) {
        cout << subword << endl;
    }
}
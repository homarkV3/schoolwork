#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;
// Function prototypes
char PrintMenu();
int GetNumOfNonWSCharacters(string);
int GetNumOfWords(string);
void ReplaceExclamation(string &);
void ShortenSpace(string &);
int FindText(string, string);
string text, phraseToFind;
// Main function
int main()
{
    // variable decalaration
    char option;
    // Reading text from user
    cout << "Enter a sample text:\n\n";
    getline(cin, text);
    // Printing text
    cout << "You entered: " << text << "\n\n";
    // Loop till user wants to quit
    do
    {
        // Printing menu
        option = PrintMenu();
    } while (option != 'Q' && option != 'q');
    // system("pause");
    return 0;
}
// Function that prints menu
char PrintMenu()
{
    char ch;
    string phraseToFind;
    // Printing menu
    cout << "MENU\n";
    cout << "c - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !'s\ns - Shorten spaces\nq - Quit\n\n";
    cout << "Choose an option:\n";
    // Reading user choice
    cin >> ch;
    // Calling functions based on option selected by //user
    switch (ch)
    {
        // User wants to quit
    case 'q':
    case 'Q':
        exit(0);
        // Counting non-whitespace characters
    case 'c':
    case 'C':
        cout << "Number of non-whitespace characters: " << GetNumOfNonWSCharacters(text) << "\n\n";
        break;
        // Counting number of words
    case 'w':
    case 'W':
        cout << "Number of words: " << GetNumOfWords(text) << "\n\n";
        break;
        // Counting number of occurrences phrase in //given string
    case 'f':
    case 'F':
        cin.ignore();
        cout << "Enter a word or phrase to be found: \n";
        getline(cin, phraseToFind);
        cout << "\"" << phraseToFind << "\" instances: " << FindText(text, phraseToFind) << "\n\n";
        break;
        // Replacing ! with .
    case 'r':
    case 'R':
        ReplaceExclamation(text);
        cout << "Edited text: " << text << "\n\n";
        break;
        // Replacing multiple spaces with single //space
    case 's':
    case 'S':
        ShortenSpace(text);
        cout << "Edited text: " << text << "\n\n";
        break;
    default:
        cout << "Invalid Choice.... Try Again\n";
        break;
    }
    return ch;
}
// Function that count number of non space characters
int GetNumOfNonWSCharacters(const string text)
{
    int cnt = 0, i;
    int len = text.size();
    // Looping over given text
    for (i = 0; i < len; i++)
    {
        // Counting spaces
        if (!isspace(text[i]))
            cnt++;
    }
    return cnt;
}
// Function that count number of words in the string
int GetNumOfWords(const string text)
{
    int words = 0, i;
    int len = text.size();
    // Looping over text
    for (i = 0; i < len; i++)
    {
        // Checking for space
        if (isspace(text[i]))
        {
            // Handling multiple spaces
            while (isspace(text[i]))
                i++;
            // Incrementing words
            i--;
            words++;
        }
    }
    // Handling last word
    words = words + 1;
    return words;
}
// Function that replaces ! with .
void ReplaceExclamation(string &text)
{
    string newText = text;
    int i, len = text.size();
    // Looping over string
    for (i = 0; i < len; i++)
    {
        // Replacing ! with .
        if (text[i] == '!')
            newText[i] = '.';
    }
    text = newText;
}
// Function that replaces Multiple spaces with single space
void ShortenSpace(string &text)
{
    int i, len = text.size(), k = 0;
    string newText = "";
    // Looping over string
    for (i = 0; i < len; i++)
    {
        // Assign individual characters
        // Handling multiple spaces
        if (isspace(text[i]))
        {
            // Replacing multiple spaces with single //space
            while (isspace(text[i]))
                i++;
            i--;
            newText += " ";
        }
        else
        {
            newText += text[i];
        }
    }
    text = newText;
}
// Function that counts the occurrences of given phrase in a //given text
int FindText(string text, string phrase)
{
    int count = 0;
    if (phrase.size() == 0)
        return 0;
    // Counting number of phrase occurrences in the given string
    for (size_t offset = text.find(phrase); offset != string::npos; offset = text.find(phrase, offset + phrase.size()))
    {
        ++count;
    }
    // Retuning count
    return count;
}
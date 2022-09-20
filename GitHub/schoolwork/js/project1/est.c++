#include <iostream>
#include <vector>
using namespace std;

// parameter order will always be jersey #s then ratings
void outputRoster(const vector<int> &, const vector<int> &);
void addPlayer(vector<int> &, vector<int> &);
void removePlayer(vector<int> &, vector<int> &);
void updatePlayerRating(const vector<int> &, vector<int> &);
void outputPlayersAboveRating(const vector<int> &, const vector<int> &);

int main()
{
    // below two lines declares two vectors
    vector<int> jerseyNumber; // vector to hold jersey number
    vector<int> playerRating; // vector to hold player rating
    int input;

    for (int i = 0; i < 5; i++) // loop iterates five times to take user input of jersey number and players rating
    {
        cout << "Enter player " << i + 1 << "'s jersey number:\n";
        cin >> input;
        jerseyNumber.push_back(input);
        cout << "Enter player " << i + 1 << "'s rating:\n";
        cin >> input;
        cout << "\n";
        playerRating.push_back(input);
    }

    outputRoster(jerseyNumber, playerRating); // calls function outputRoster to output the roster
    char choice;
    while (1) // loop iterates until user enters q to quit
    {
        cout << "\nMENU\n";
        cout << "a - Add player\n";
        cout << "d - Remove player\n";
        cout << "u - Update player rating\n";
        cout << "r - Output players above a rating\n";
        cout << "o - Output roster\n";
        cout << "q - Quit\n\nChoose an option:\n";
        cin >> choice;

        switch (choice) // control jumps over user input and then that corresponding function gets executed
        {
        case 'a':
            addPlayer(jerseyNumber, playerRating); // calls function addPlayer
            break;
        case 'd':
            removePlayer(jerseyNumber, playerRating); // calls function removePlayer
            break;
        case 'u':
            updatePlayerRating(jerseyNumber, playerRating); // calls function updatePlayerRating
            break;
        case 'r':
            outputPlayersAboveRating(jerseyNumber, playerRating); // calls function outputPlayersAboveRating
            break;
        case 'o':
            outputRoster(jerseyNumber, playerRating); // calls function outputRoster
            break;
        case 'q':
            exit(0); // terminates the program
        default:
            cout << "Wrong Choice\n";
        }
    }

    return 0;
}

void outputRoster(const vector<int> &jerseyNumber, const vector<int> &playerRating)
{

    cout << "ROSTER\n";
    for (int i = 0; i < jerseyNumber.size(); ++i) // loop iterates to print roster
    {
        cout << "Player " << i + 1 << " -- Jersey number: " << jerseyNumber[i] << ", Rating: " << playerRating[i] << "\n";
    }
}

void addPlayer(vector<int> &jerseyNumber, vector<int> &playerRating)
{

    int input;
    cout << "Enter a new player's jersey number:\n"; // prompts user to enter jersey number
    cin >> input;
    jerseyNumber.push_back(input);              // adds the jersey number to vector
    cout << "Enter the player's rating:\n"; // // prompts user to enter rating
    cin >> input;
    playerRating.push_back(input); // adds the rating to vector
}

void removePlayer(vector<int> &jerseyNumber, vector<int> &playerRating)
{

    int input, j = 0;
    cout << "Enter a jersey number:\n";
    cin >> input;
    for (int i = 0; i < jerseyNumber.size(); ++i)
    {
        if (jerseyNumber[i] != input) // checks if given jersey number matches than skips that jersey number
        {
            // below code will not add the user input jersey number to the vector and hence will get removed
            jerseyNumber[j] = jerseyNumber[i];
            playerRating[j] = playerRating[i];
            j++;
        }
    }
    jerseyNumber.resize(jerseyNumber.size() - 1); // resizes the vector by removing 1 extra elements
    playerRating.resize(playerRating.size() - 1); // resizes the vector by removing 1 extra elements
}

void updatePlayerRating(const vector<int> &jerseyNumber, vector<int> &playerRating)
{

    int inputRating, inputJersey;
    cout << "Enter a jersey number:\n";
    cin >> inputJersey;
    cout << "Enter a new rating for player:\n";
    cin >> inputRating;

    for (int i = 0; i < jerseyNumber.size(); ++i)
    {
        if (jerseyNumber[i] == inputJersey) // checks if user input jersey number matches or not
        {
            playerRating[i] = inputRating; // updates the rating
            break;
        }
    }
}

void outputPlayersAboveRating(const vector<int> &jerseyNumber, const vector<int> &playerRating)
{

    int input;
    cout << "Enter a rating:\n";
    cin >> input;
    cout << "ABOVE " << input << "\n";
    int j = 1;
    for (int i = 0; i < jerseyNumber.size(); ++i)
    {
        if (input < playerRating[i]) // checks if players rating is above user input rating then displays the information
        {
            cout << "Player " << j << " -- Jersey number: " << jerseyNumber[i] << ", Rating: " << playerRating[i] << "\n";
        }
        j++;
    }
}
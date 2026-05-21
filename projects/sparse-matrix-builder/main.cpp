#include <iostream>
#include <vector>

using namespace std;

int main() {
    int rows, cols;
    cin >> rows >> cols;

    vector<vector<int>> matrix(rows, vector<int>(cols, 0));

    int entries;
    cin >> entries;

    for (int i = 0; i < entries; i++) {
        int row, col, value;
        cin >> row >> col >> value;

        if (row >= 0 && row < rows && col >= 0 && col < cols) {
            matrix[row][col] = value;
        }
    }

    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            if (col > 0) {
                cout << " ";
            }
            cout << matrix[row][col];
        }
        cout << endl;
    }

    return 0;
}

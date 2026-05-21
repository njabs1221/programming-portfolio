#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

struct Move {
    string name;
    int dx;
    int dy;
};

int main() {
    int cols, rows;
    cin >> cols >> rows;

    int appleX, appleY;
    cin >> appleX >> appleY;

    int segments;
    cin >> segments;

    vector<vector<int>> grid(rows, vector<int>(cols, 0));
    grid[appleY][appleX] = 5;

    int headX = 0;
    int headY = 0;

    for (int segment = 1; segment <= segments; segment++) {
        int x1, y1, x2, y2, x3, y3;
        cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

        grid[y1][x1] = segment;
        grid[y2][x2] = segment;
        grid[y3][x3] = segment;

        if (segment == 1) {
            headX = x1;
            headY = y1;
        }
    }

    vector<Move> moves = {
        {"DOWN", 0, 1},
        {"LEFT", -1, 0},
        {"RIGHT", 1, 0},
        {"UP", 0, -1},
    };

    double bestDistance = 1e18;
    vector<string> bestMoves;

    for (const Move &move : moves) {
        int nextX = headX + move.dx;
        int nextY = headY + move.dy;

        if (nextX < 0 || nextX >= cols || nextY < 0 || nextY >= rows) {
            continue;
        }

        int cell = grid[nextY][nextX];
        if (cell >= 1 && cell <= 4) {
            continue;
        }

        double distance = hypot(nextX - appleX, nextY - appleY);

        if (distance < bestDistance) {
            bestDistance = distance;
            bestMoves.clear();
            bestMoves.push_back(move.name);
        } else if (distance == bestDistance) {
            bestMoves.push_back(move.name);
        }
    }

    sort(bestMoves.begin(), bestMoves.end());

    for (const string &move : bestMoves) {
        cout << move << endl;
    }

    return 0;
}

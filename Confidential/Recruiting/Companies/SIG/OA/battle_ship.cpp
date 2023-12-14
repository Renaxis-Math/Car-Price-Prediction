#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;

vector<string> solution(vector<vector<int>>& grid, vector<pair<int, int>>& shots) {
    map<int, set<pair<int, int>>> ship_indices_map;

    for (int r = 0; r < grid.size(); ++r) {
        for (int c = 0; c < grid[0].size(); ++c) {
            int ship = grid[r][c];
            if (ship_indices_map.find(ship) == ship_indices_map.end()) {
                ship_indices_map[ship] = set<pair<int, int>>();
            }
            ship_indices_map[ship].insert(make_pair(r, c));
        }
    }

    vector<string> answers;

    for (auto& shot : shots) {
        int r = shot.first;
        int c = shot.second;

        if (grid[r][c] == 0) {
            answers.push_back("Missed");
        } else {
            if (grid[r][c] == -1) {
                answers.push_back("Already attacked");
            } else {
                int ship = grid[r][c];
                grid[r][c] = -1;
                ship_indices_map[ship].erase(make_pair(r, c));
                if (ship_indices_map[ship].empty()) {
                    answers.push_back("Ship " + to_string(ship) + " sunk");
                } else {
                    answers.push_back("Attacked ship " + to_string(ship));
                }
            }
        }
    }

    return answers;
}
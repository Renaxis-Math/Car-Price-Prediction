#include <bits/stdc++.h>
using namespace std;

bool is_valid(pair<int, int> cell, int n_row, int n_col) {
    int r = cell.first;
    int c = cell.second;
    return (0 <= r && r < n_row) && (0 <= c && c < n_col);
}

int get_distance(pair<int, int> cell1, pair<int, int> cell2) {
    int x1 = cell1.first;
    int y1 = cell1.second;
    int x2 = cell2.first;
    int y2 = cell2.second;

    return abs(x1 - x2) + abs(y1 - y2);
}

int get_min_distance(const vector<pair<int, int>>& monsters_cells, pair<int, int> cell, int& n, int& m) {
    int min_distance = n + m - 2;
    for (const auto& monsters_cell : monsters_cells) {
        min_distance = min(min_distance, get_distance(monsters_cell, cell));
    }
    return min_distance;
}


int find_distance(pair<int, int> cell, map<pair<int, int>, int>& cell_closestMonsterDistance, const vector<pair<int, int>>& monsters_cells, int& n, int& m) {
    if (cell_closestMonsterDistance.find(cell) == cell_closestMonsterDistance.end()) {
        cell_closestMonsterDistance[cell] = get_min_distance(monsters_cells, cell, n, m);
    }
    return cell_closestMonsterDistance[cell];
}

bool mid_or_below_does_not_solve(int value, pair<int, int>& start_cell, pair<int, int>& end_cell, map<pair<int, int>, int>& cell_closestMonsterDistance, const vector<pair<int, int>>& monsters_cells, int& n, int& m) {
    int start_cell_min_distance = find_distance(start_cell, cell_closestMonsterDistance, monsters_cells, n, m);
    if (start_cell_min_distance < value) {
        return false;
    }

    priority_queue<tuple<int, int, int>> queue;
    queue.push(make_tuple(-start_cell_min_distance, start_cell.first, start_cell.second));
    
    map<pair<int, int>, int> level;
    map<pair<int, int>, pair<int, int>> parent;
    int nextLevel = 1;
    
    while (!queue.empty()) {
        int cur_length = queue.size();
        for (int i = 0; i < cur_length; ++i) {
            int neg_distance, row, col;
            tie(neg_distance, row, col) = queue.top();
            queue.pop();
            pair<int, int> cell = make_pair(row, col);
            if (cell == end_cell) {
                return true;
            }
            
            vector<pair<int, int>> moves = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
            for (const auto& move : moves) {
                int next_row = row + move.first;
                int next_col = col + move.second;
                pair<int, int> next_cell = make_pair(next_row, next_col);
                if (is_valid(next_cell, n, m) && level.find(next_cell) == level.end()) {
                    int next_cell_min_distance = find_distance(next_cell, cell_closestMonsterDistance, monsters_cells, n, m);
                    if (!(next_cell_min_distance < value)) {
                        level[next_cell] = nextLevel;
                        parent[next_cell] = cell;
                        queue.push(make_tuple(-next_cell_min_distance, next_row, next_col));
                    }
                }
            }
        }
        nextLevel++;
    }
    
    return false;
}

int findBestPath(int n, int m, int startRow, int startColumn, int endRow, int endColumn, vector<int> monsterRow, vector<int> monsterColumn) {
    vector<pair<int, int>> monsters_cells;
    pair<int, int> start_cell;
    pair<int, int> end_cell;
    map<pair<int, int>, int> cell_closestMonsterDistance;
    
    for (int i = 0; i < monsterRow.size(); ++i) {
        monsters_cells.emplace_back(monsterRow[i], monsterColumn[i]);
    }
    
    start_cell = make_pair(startRow, startColumn);
    end_cell = make_pair(endRow, endColumn);
    
    int min_distance = 0;
    int max_distance = n + m - 2;

    int left = min_distance;
    int right = max_distance;
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        bool is_mid_big_enough = mid_or_below_does_not_solve(mid, start_cell, end_cell, cell_closestMonsterDistance, monsters_cells, n, m);
        if (is_mid_big_enough) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    return left - 1;
}
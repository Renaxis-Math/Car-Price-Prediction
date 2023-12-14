#include <bits/stdc++.h>
using namespace std;

using pi = pair<int, int>;

bool is_valid(pi& cell, int n_row, int n_col) {
    /* Return True if a cell is within boundary of the given grid. */
    int r = cell.first, c = cell.second;
    return (0 <= r && r < n_row) && (0 <= c && c < n_col);
}

int get_distance(pi& cell_1, pi& cell_2) {
    /* Return the Euclidean distance between 2 cells. */
    int x1 = cell_1.first, y1 = cell_1.second;
    int x2 = cell_2.first, y2 = cell_2.second;

    return abs(x1 - x2) + abs(y1 - y2);
}

int get_min_distance_to_anyMonsters(const vector<pi>& monsters_cells, pi& cell, int n, int m) {
    /*
    Return the minimum distance of input cell to any monster in 'monsters_cells'
    */
    int min_distance = n + m - 2; // Maximize initialization for later comparison.

    for (const auto& monsters_cell : monsters_cells) {
        min_distance = min(min_distance, get_distance(monsters_cell, cell));
    }

    return min_distance;
} // O(n)

int findBestPath(int n, int m, int startRow, int startColumn, int endRow, int endColumn, vector<int> monsterRow, vector<int> monsterColumn) {

    auto retrieve_minDistToMonster = [&](cell) {
        /* Memoize get_min_distance_to_anyMonsters() if called with same inputs and return its value. */
        if (cell_minDistToMonster.find(cell) == cell_minDistToMonster.end()) { 
            cell_minDistToMonster[cell] = get_min_distance_to_anyMonsters(monsters_cells, cell, n, m); 
        }

        return cell_minDistToMonster[cell];        
    }

    auto mid_or_below_does_not_solve - [&](value) {
        /* Return True if you can find the path with the minimum distance to any monsters == 'value' */
        int start_cell_min_distance = retrieve_minDistToMonster(start_cell);
        if (start_cell_min_distance < value) { return false; }

        priority_queue<tuple<int, int, int>> queue; // Max Heap
        queue.push(make_tuple(-start_cell_min_distance, start_cell.first, start_cell.second));
        
        map<pi, int> seenCell_level;
        int next_level = 1; // For debugging: tracing paths
        
        while (!queue.empty()) { // O(mn)
            int cur_length = queue.size();

            for (int i = 0; i < cur_length; ++i) {
                int neg_distance, cur_row, cur_col;
                tie(neg_distance, cur_row, cur_col) = queue.top();
                queue.pop(); // O(log mn)

                if (make_pair(cur_row, cur_col) == end_cell) { return true; } // Desired path found
                
                for (const auto& move : moves) {
                    pi next_cell = make_pair(cur_row + move.first, cur_col + move.second);

                    if (is_valid(next_cell, n, m) && seenCell_level.find(next_cell) == seenCell_level.end()) {
                        int next_cell_min_distance = retrieve_minDistToMonster(next_cell);

                        if (!(next_cell_min_distance < value)) {
                            seenCell_level[next_cell] = next_level;
                            queue.push(make_tuple(-next_cell_min_distance, next_row, next_col));
                        }
                    }
                }
            }
            ++next_level;
        }
        
        return false;        
    } // O(mn * log(mn))
    
    pi start_cell = make_pair(startRow, startColumn), end_cell = make_pair(endRow, endColumn);
    map<pi, int> cell_minDistToMonster;
    
    vector<pi> monsters_cells;
    for (int i = 0; i < monsterRow.size(); ++i) { monsters_cells.emplace_back(monsterRow[i], monsterColumn[i]); } // O(k)
    
    vector<pi> moves = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    
    /* Binary Search: if we find a path having minimum
    distance to any monsters == 'mid', all values
    fewer than 'mid' are eliminated. Continue exploring from 'mid' + 1 */
    int left = 0, right = n + m - 2; // ~ get_distance(start_cell, end_cell);;

    while (left < right) {
        int mid = left + (right - left) / 2;
        
        bool is_mid_big_enough = mid_or_below_does_not_solve(mid);
        
        if (is_mid_big_enough) { left = mid + 1; } 
        else { right = mid; }
    } // O(log mn)
    
    /* everytime 'mid' satisfies our condition function, 'left' increases. 
    Thus, 'left' is running ahead of actual result by 1. */
    return left - 1;
}
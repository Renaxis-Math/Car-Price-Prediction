#include <iostream>
using namespace std;

/*
 * Complete the 'numberOfTokens' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER expiryLimit
 *  2. 2D_INTEGER_ARRAY commands
 */

int numberOfTokens(int expiryLimit, vector<vector<int>> commands) {
    unordered_map<int,int> tokenID_expiryTime_map;
    int time = 0;
    
    for (int c = 0; c < commands.size(); c++) {
        int action = commands[c][0], tokenID = commands[c][1];
        time = commands[c][2];
        
        // Create
        if (action == 0){ tokenID_expiryTime_map[tokenID] = expiryLimit + time; }

        // Reset
        else if(action == 1){
            if(tokenID_expiryTime_map.count(tokenID)) {
                int expiry_time = tokenID_expiryTime_map[tokenID];
                if(!(expiry_time < time)) { tokenID_expiryTime_map[tokenID] = time + expiryLimit; }
            }
        }
    }
    

    int activeToken_count = 0;
    for (const auto& element : tokenID_expiryTime_map) {
        if(element.second >= time){ ++activeToken_count; }  
    }

    return activeToken_count;    
}
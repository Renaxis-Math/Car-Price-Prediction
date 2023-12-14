enum USED_FOR
{
    EMPTY = 0,
    ENTER,
    EXIT
};

vector<int> timeTaken(vector<int>& arrival, vector<int>& state) {
    int t = 0, i = 0;
    int n = arrival.size();
    int max_t = arrival[n - 1] + n;
    USED_FOR used_for = EMPTY;
    priority_queue<int, vector<int>, std::greater<int>> enter, exit;
    vector<int> ans(n, -1);
    while (t <= max_t)
    {
        while (i < n && arrival[i] <= t)
        {
            if (state[i] == 0)
            {
                enter.push(i);
            }
            else
            {
                exit.push(i);
            }
            i++;
        }

        switch(used_for)
        {
        case EMPTY:
            if (!exit.empty())
            {
                int idx = exit.top();
                exit.pop();
                ans[idx] = t;
                used_for = EXIT;
            }
            else if (!enter.empty())
            {
                int idx = enter.top();
                enter.pop();
                ans[idx] = t;
                used_for = ENTER;
            }
            break;
        case EXIT:
            if (!exit.empty())
            {
                int idx = exit.top();
                exit.pop();
                ans[idx] = t;
                used_for = EXIT;
            }
            else if (!enter.empty())
            {
                int idx = enter.top();
                enter.pop();
                ans[idx] = t;
                used_for = ENTER;
            }
            else
            {
                used_for = EMPTY;
            }
            break;
        case ENTER:
            if (!enter.empty())
            {
                int idx = enter.top();
                enter.pop();
                ans[idx] = t;
                used_for = ENTER;
            }
            else if (!exit.empty())
            {
                int idx = exit.top();
                exit.pop();
                ans[idx] = t;
                used_for = EXIT;
            }
            else
            {
                used_for = EMPTY;
            }
        }
        t++;
    }
    return ans;
}
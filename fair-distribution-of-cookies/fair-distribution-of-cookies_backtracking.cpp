class Solution
{
public:
    int unfairness = INT_MAX;
    vector<int> dsitribution;

    int distributeCookies(vector<int> &cookies, int k)
    {
        dsitribution = vector<int>(k, 0);
        distributeCookiesRec(cookies, k);
        return unfairness;
    }

    void distributeCookiesRec(vector<int> &cookies, int k, int counter = 0)
    {
        if (counter == cookies.size())
        {
            int sum = dsitribution[0] + dsitribution[1];
            calculate_unfairness();
            return;
        }

        for (int j = 0; j < k; j++)
            {
                dsitribution[j] += cookies[counter];
                distributeCookiesRec(cookies, k, counter + 1);
                dsitribution[j] -= cookies[counter];
            }
        return;
    }

    void calculate_unfairness()
    {
        int max = INT_MIN;
        for (auto &i : dsitribution)
        {
            if (i > max)
            {
                max = i;
            }
        }
        if (max < unfairness)
        {
            unfairness = max;
        }
    }
};

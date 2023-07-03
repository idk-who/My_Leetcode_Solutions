class Solution
{
public:
    bool buddyStrings(string s, string goal)
    {
        if (s.size() != goal.size())
            return false;

        vector<vector<char>> diff;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] != goal[i])
                diff.push_back({s[i], goal[i]});
        }

        if (diff.size() == 2)
            return (diff[0][0] == diff[1][1] && diff[0][1] == diff[1][0]);
        else if (diff.size() == 0)
        {
            vector<int> freq(26, 0);
            for (int i = 0; i < s.size(); i++)
            {
                freq[s[i] - 'a']++;
            }
            for (int i = 0; i < 26; i++)
            {
                if (freq[i] > 1)
                    return true;
            }
        }
        return false;
    }
};

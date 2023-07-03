class Solution
{
public:
    bool buddyStrings(string s, string goal)
    {
        if (s.size() != goal.size())
            return false;

        vector<vector<char>> different;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] != goal[i])
                different.push_back({s[i], goal[i]});
        }

        if (different.size() == 2 and different[0][0] == different[1][1] and different[0][1] == different[1][0])
            return true;
        else if (different.size() == 0)
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
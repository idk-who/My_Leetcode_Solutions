class Solution {
public:
    vector<vector<int>> traced;
    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
        int day = 0;
        int low = 0;
        int high = cells.size()-1;    
        int mid = low + ((high - low)/2);
        
        while(low<=high){
            if (mazeSolveMain(row, col, cells, mid)){
                low = mid+1;
            }
            else{
                high = mid-1;
            }
            mid = low + ((high - low)/2);
        }
        return mid;
    }

    bool mazeSolveMain(int row, int col, vector<vector<int>>& cells, int mid){
        vector<vector<int>> maze (row, vector<int> (col, 1));
        traced = maze;
        for (int i = 0; i <= mid; i++){
            maze[cells[i][0]-1][cells[i][1]-1] = 0;
        }
        traced = maze;
        return maizeSolveAll(maze);
    }

    bool maizeSolveAll(vector<vector<int>>& maze){
        for (int j=0; j<maze[0].size(); j++){
            if (solveMaze(maze, 0, j)) return true;
        }
        return false;
    }

    bool solveMaze(vector<vector<int>>& maze, int i, int j){
        if (!isSafe(maze, i, j)){
            return false;
        }

        traced[i][j] = 0; 
         
        if (i==maze.size()-1) return true;

        if (solveMaze(maze, i+1, j)) return true;
        else if (solveMaze(maze, i, j+1)) return true;
        else if (solveMaze(maze, i, j-1)) return true;
        else if (solveMaze(maze, i-1, j)) return true;

        return false;
    }

    bool isSafe(vector<vector<int>>& maze, int i, int j){
        return (i>=0 && j>=0 && i<maze.size() && j<maze[0].size() && maze[i][j] == 1 && traced[i][j] == 1);
    }

};

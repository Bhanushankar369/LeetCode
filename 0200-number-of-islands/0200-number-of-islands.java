class Solution {
    public int numIslands(char[][] grid) {
        int count=0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j] == '1'){
                    count+=1;
                    dfs(i, j, grid);
                }
            }
        }
        return count;
    }
    void dfs(int row, int col, char[][] grid){
        if(row < 0 || row >= grid.length || col < 0 || col >= grid[0].length || grid[row][col] != '1'){
            return ;
        }
        grid[row][col] = '*';

        dfs(row-1, col, grid);
        dfs(row+1, col, grid);
        dfs(row, col-1, grid);
        dfs(row, col+1, grid);
    }
}
class Solution {
    private List<String> res = new ArrayList<>();
    private List<String> path = new ArrayList<>();

    public List<String> generateParenthesis(int n) {
        dfs(n, n);
        return res;
    }

    void dfs(int open, int close){
        if(open == 0 && close == 0){
            String output = String.join("", path);
            res.add(output);
            return;
        }

        if(open > 0){
            path.add("(");
            dfs(open - 1, close);
            path.remove(path.size() - 1);
        }

        if (close > open){
            path.add(")");
            dfs(open, close - 1);
            path.remove(path.size() - 1);
        }

    }
}
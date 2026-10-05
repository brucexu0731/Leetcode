class Solution {
    public int scoreOfParentheses(String s) {
        
        Deque<Integer> parens = new ArrayDeque<>();
        Deque<Integer> scores = new ArrayDeque<>();
        int res = 0;

        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (c == '('){
                parens.addLast(i);
                scores.addLast(0);
            } else{
                parens.pollLast();

                int score = scores.pollLast();
                if (score == 0){
                    score = 1;
                } else{
                    score *= 2;
                }
                
                if (scores.size() == 0){
                    res += score;
                } else{
                    score += scores.pollLast();
                    scores.addLast(score);
                }
            }
        }

        return res;
    }
}
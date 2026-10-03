class Solution {
    public int longestValidParentheses(String s) {
        
        Deque<Integer> stack = new ArrayDeque<>();
        int res = 0;
        int prevInvalid = -1;

        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            //open parenthesis, add to stack
            if(c == '('){
                stack.addLast(i);
            }
            
            //closed parenthesis, check if there's matching open paren first, if not set breakpoint
            //prevInvalid. If there is matching open paren, we can first extend the length to 
            //the next open parenthesis in the stack, if there are no blocking open parenthesis left, we can extend again to the previous invalid breakpoint 
            else{ 
                if (stack.size() == 0){
                    prevInvalid = i;
                } else {
                    stack.removeLast();
                    if (stack.size() == 0){
                        res = Math.max(res, i - prevInvalid);
                    } else{
                        res = Math.max(res, i - stack.peekLast());
                    }
                }
            }
        }

        return res;
    }
}
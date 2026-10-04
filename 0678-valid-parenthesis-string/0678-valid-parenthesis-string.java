class Solution {
    public boolean checkValidString(String s) {
        
        //should've used deque
        List<Integer> opens = new ArrayList<>();
        List<Integer> stars = new ArrayList<>();

        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c == '('){
                opens.add(i);
            } else if (c == '*'){
                stars.add(i);
            } else {
                if(opens.size() > 0){
                    opens.remove(opens.size() - 1);
                } else if (stars.size() > 0){
                    stars.remove(stars.size() - 1);
                } else {
                    return false;
                }
            }
        }

        while(opens.size() > 0){
            if(stars.size() <= 0 || stars.get(stars.size() - 1) < opens.get(opens.size() - 1)){
                return false;
            }
            opens.remove(opens.size() - 1);
            stars.remove(stars.size() - 1);
        }

        return true;
    }
}
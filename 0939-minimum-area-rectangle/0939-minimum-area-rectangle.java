class Solution {
    public int minAreaRect(int[][] points) {
        record Point(int x, int y){}

        Set<Point> set = new HashSet<>();
        
        int res = 0;

        for (int i = 0; i < points.length; i++){
            int x = points[i][0];
            int y = points[i][1];
            set.add(new Point(x, y));
        }

        for(int i = 0; i < points.length; i++){
            int x1 = points[i][0];
            int y1 = points[i][1];
            for(int j = i + 1; j < points.length; j++){
                int x2 = points[j][0];
                int y2 = points[j][1];
                if (x1 == x2 || y1 == y2){
                    continue;
                }
                if (set.contains(new Point(x1, y2)) && set.contains(new Point(x2, y1))){
                    int area = Math.abs(x1 - x2) * Math.abs(y1 - y2);
                    if (res == 0){
                        res = area;
                    } else {
                        res = Math.min(area, res);
                    }
                }
            }
        }

        return res;


    }
}
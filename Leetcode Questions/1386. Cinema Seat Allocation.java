// Solution 


class Solution {
    public int maxNumberOfFamilies(int n, int[][] reservedSeats) {
        
        int m = reservedSeats.length;

        Arrays.sort(reservedSeats, (a, b) -> {
            if (a[0] != b[0]) { return a[0] - b[0]; }
            return a[1] - b[1];
        });

        int ans = 0;
        int reservedRows =  0;
        for(int i = 0; i < reservedSeats.length; reservedRows++)
        {
            int row = reservedSeats[i][0];
            boolean[] seats = new boolean[11];

            for ( ;
                i < reservedSeats.length &&
                    reservedSeats[i][0] == row; 
                i++
            ) seats[reservedSeats[i][1]] = true;

            int count = 0;

            if (!seats[2] && !seats[3] &&
                !seats[4] && !seats[5]
            ) { count++; }

            if (!seats[6] && !seats[7] &&
                !seats[8] && !seats[9]
            ) { count++; }

            if (count == 0) 
            {
                if (!seats[4] && !seats[5] &&
                    !seats[6] && !seats[7]
                ) { count++; }
            }
            ans += count;

        } ans += (n - reservedRows) * 2;

        return ans;
    }
}
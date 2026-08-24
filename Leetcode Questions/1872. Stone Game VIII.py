# Soution

class Solution {

    private int solve(int[] pref, int i) {

        // Base case
        if (i == pref.length - 1) {
            return pref[i];
        }

        int next = solve(pref, i + 1);

        int take = pref[i] - next;
        int skip = next;

        return Math.max(take, skip);
    }

    public int stoneGameVIII(int[] stones) {

        int n = stones.length;

        int[] pref = new int[n];

        // Build prefix sum
        pref[0] = stones[0];

        for (int i = 1; i < n; i++) {
            pref[i] = pref[i - 1] + stones[i];
        }

        return solve(pref, 1);
    }
}
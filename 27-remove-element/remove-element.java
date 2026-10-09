class Solution {
    public int removeElement(int[] nums, int val) {
        int n = nums.length;
        int j = 1;

        for (int i = 0; i < n; i++) {
            if (nums[i] == val) {
                if (j <= i) j = i + 1;                 
                while (j < n && nums[j] == val) j++;    
                if (j == n) break;                     

                int temp = nums[i];                    
                nums[i] = nums[j];
                nums[j] = temp;
                j++;
            }
        }

        int k = 0;                                     
        for (int x : nums) if (x != val) k++;
        return k;
    }
        
    
}
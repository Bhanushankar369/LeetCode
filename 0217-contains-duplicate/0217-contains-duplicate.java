class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> new_arr = new HashSet();
        for(int num: nums){
            if(new_arr.contains(num)){
                return true;
            }
            new_arr.add(num);
        }
        return false;
    }
}
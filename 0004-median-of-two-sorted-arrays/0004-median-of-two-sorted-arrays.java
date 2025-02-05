class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] mix = new int[nums1.length + nums2.length];
        int i=0;
        int j=0;
        int k=0;
        while(i<nums1.length && j<nums2.length){
            if(nums1[i] < nums2[j]){
                mix[k] = nums1[i];
                i++;
            }else{
                mix[k] = nums2[j];
                j++;
            }
            k++;
        }
        while(i<nums1.length){
            mix[k] = nums1[i];
            i++;
            k++;
        }
        while(j<nums2.length){
            mix[k] = nums2[j];
            j++;
            k++;
        }
        int ind = mix.length/2;
        double mid = 0.0;
        if(mix.length % 2 == 0){
            mid = (mix[ind] + mix[ind-1])/2.0;
        }else{
            mid = mix[ind];
        }
        return mid;
    }
}
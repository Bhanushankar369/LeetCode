class Solution {
    public String mergeAlternately(String word1, String word2) {
        int i=0;
        int j=0;
        String s = "";
        while(i<word1.length() && j<word2.length()){
            s+=word1.charAt(i);
            s+=word2.charAt(j);
            i++;
            j++;
        }
        if(i<word1.length()){
            s+=word1.substring(i,word1.length());
        }
        if(j<word2.length()){
            s+=word2.substring(j,word2.length());
        }
        return s;
    }
}
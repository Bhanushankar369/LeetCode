class Solution {
    public List<String> stringMatching(String[] words) {
        List<String> list = new ArrayList<>();
        for(int i=0;i<words.length;i++){
            for(int j=0;j<words.length;j++){
                if((!words[j].equals(words[i]) && words[i].contains(words[j]))){
                    if(!list.contains(words[j])){
                        list.add(words[j]);
                    }
                }
            }
        }
        return list;
    }
}
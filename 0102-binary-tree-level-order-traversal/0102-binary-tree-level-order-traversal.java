/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if(root == null){
            return ans;
        }
        Deque<TreeNode> dq = new ArrayDeque();
        dq.add(root);
        while (!dq.isEmpty()){
            List<Integer> level = new ArrayList<>();
            int len = dq.size();

            for(int i=0;i<len;i++){
                TreeNode ele = dq.removeFirst();
                level.add(ele.val);
                if(ele.left != null){
                    dq.add(ele.left);
                }
                if(ele.right != null){
                    dq.add(ele.right);
                }
            }
            ans.add(level);
        }
        return ans;
    }
}
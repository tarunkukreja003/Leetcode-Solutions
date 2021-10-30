/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        
	//Initialising a variable to count the
	//height of tree
	int depth = 0;
    
    if (root == NULL) {
        return 0;
    }

	queue<TreeNode*>q;
	
	//Pushing first level element along with NULL
	q.push(root);
	q.push(NULL);
	while(!q.empty()){
		TreeNode* temp = q.front();
		q.pop();
	
		//When NULL encountered, increment the value
		if(temp == NULL){
			depth++;
		}
		
		//If NULL not encountered, keep moving
		if(temp != NULL){
			if(temp->left){
				q.push(temp->left);
			}
			if(temp->right){
				q.push(temp->right);
			}
		}
	
		//If queue still have elements left,
		//push NULL again to the queue.
		else if(!q.empty()){
			q.push(NULL);
		}
	}
	return depth;
        
    }
};
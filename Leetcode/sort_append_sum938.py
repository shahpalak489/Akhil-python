# class Solution:
# 	def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
# 		null=0
# 		newlist=sorted(root)#print(newlist)
# 		final_list=[]
# 		for x in newlist:
# 			if x>=L and x<=R:
# 				final_list.append(x)#print (final_list)
# 				b=sum(final_list)
# 				return b

# root1=[10,5,15,3,7,null,18]
# rangeSumBST(root1,7,15)


class Solution:
	def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
		null=0
		root.sort()
		print(root)

root=[10,5,15,3,7,null,18]
rangeSumBST(root1,7,15)
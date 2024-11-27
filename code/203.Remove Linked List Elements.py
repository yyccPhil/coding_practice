#
# @lc app=leetcode id=203 lang=python3
# @lcpr version=20003
#
# [203] Remove Linked List Elements
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # dummy head, to easier deal with removing first node
        dummy  = ListNode(None)
        dummy.next = head
        cur = dummy
        
        while cur.next:
            if cur.next.val == val:
                cur.next.val = None
                cur.next = cur.next.next
            else:
                cur = cur.next
                
        return dummy.next
        
        
# @lc code=end



#
# @lcpr case=start
# [1,2,6,3,4,5,6]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n1\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7]\n7\n
# @lcpr case=end

#


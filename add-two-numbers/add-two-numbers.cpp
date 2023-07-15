/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* answer = new ListNode();

        ListNode *tempNode = answer;
        int tempNum = 0;
        int carry = 0;
        while ((l1 != nullptr) || (l2 != nullptr)){
            tempNum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
            carry = tempNum / 10;
            tempNode->next = new ListNode(tempNum % 10);

            l1 = l1 ? l1->next : nullptr;
            l2 = l2 ? l2-> next: nullptr;
            tempNode =tempNode->next;
        }

        if (carry) tempNode->next = new ListNode(carry);

        return answer->next;
    }
};
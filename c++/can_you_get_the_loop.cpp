typedef struct node_t Node;
struct node_t
{
    const Node *next;
};

int loop_size(const Node *node)
{
    const Node *slow = node->next;
    const Node *fast = node->next->next;
    while (slow != fast)
    {
        slow = slow->next;
        fast = fast->next->next;
    }
    slow = node;
    while (slow != fast)
    {
        slow = slow->next;
        fast = fast->next;
    }
    int lam = 1;
    fast = fast->next;
    while (slow != fast)
    {
        fast = fast->next;
        lam++;
    }
    return lam;
}
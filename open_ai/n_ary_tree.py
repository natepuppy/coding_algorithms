
# =============================================================================
# Distributed tree node count
#
# Each node of the tree represents a real machine in a cluster. Each machine
# can only communicate with its parent and child nodes through "nodeId" using:
#   sendAsyncRequest(toNodeId, message)   — provided, just call it
#   receiveRequest(fromNodeId, message)   — YOU implement this
#
# Root (node 1) needs to count total machines in the cluster and print it.
#
#           node1
#          /      \
#        node2    node3
#        /           \
#      node4        node5
#      /   \          /   \
#    node6  node7   node8  node9
#
# =============================================================================

# Global registry: nodeId -> Node instance (simulates the cluster network)
cluster = {}

def sendAsyncRequest(to_node_id, message):
    cluster[to_node_id].receiveRequest(message["from"], message)

    
REQUEST = "REQUEST"
REPLY = "REPLY"


class Node:
    def __init__(self, node_id, parent_id, children_ids):
        self.node_id = node_id
        self.parent_id = parent_id
        self.children_ids = children_ids
        cluster[node_id] = self

        self.replies_received = 0
        self.subtree_count = 0

    def start_count(self):
        """Root calls this to kick off the count."""
        if not self.children_ids:
            # single-node tree
            print(1)
            return

        for child_id in self.children_ids:
            sendAsyncRequest(child_id, {"from": self.node_id, "type": REQUEST})

    def receiveRequest(self, from_node_id, message):
        msg_type = message["type"]

        if msg_type == REQUEST:
            # parent asked me to count my subtree
            if not self.children_ids:
                # leaf: my subtree is just me (1)
                sendAsyncRequest(self.parent_id, {
                    "from": self.node_id,
                    "type": REPLY,
                    "count": 1,
                })
            else:
                # forward the request to all my children
                for child_id in self.children_ids:
                    sendAsyncRequest(child_id, {"from": self.node_id, "type": REQUEST})

        elif msg_type == REPLY:
            # a child reported its subtree size
            self.subtree_count += message["count"]
            self.replies_received += 1

            # have all children replied?
            if self.replies_received == len(self.children_ids):
                total = self.subtree_count + 1  # +1 for myself

                if self.parent_id is None:
                    # I'm root — done
                    print(total)
                else:
                    # send my total up to my parent
                    sendAsyncRequest(self.parent_id, {
                        "from": self.node_id,
                        "type": REPLY,
                        "count": total,
                    })

if __name__ == "__main__":
    Node(6, 4, [])
    Node(7, 4, [])
    Node(8, 5, [])
    Node(9, 5, [])
    Node(4, 2, [6, 7])
    Node(5, 3, [8, 9])
    Node(2, 1, [4])
    Node(3, 1, [5])
    Node(1, None, [2, 3])
    cluster[1].start_count()
    # should print: 9




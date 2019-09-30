#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/module.h>
#include <asm/current.h>
#include <asm/ptrace.h>
#include <linux/sched.h>
#include <linux/cred.h>
#include <asm/unistd.h>
#include <linux/spinlock.h>
#include <linux/semaphore.h>
#include <linux/syscalls.h>
#include "interceptor.h"


MODULE_DESCRIPTION("My kernel module");
MODULE_AUTHOR("Mohammad Abufardeh and Anthony Chu");
MODULE_LICENSE("GPL");

//----- System Call Table Stuff ------------------------------------
/* Symbol that allows access to the kernel system call table */
extern void* sys_call_table[];

/* The sys_call_table is read-only => must make it RW before replacing a syscall */
void set_addr_rw(unsigned long addr) {

	unsigned int level;
	pte_t *pte = lookup_address(ad…
[5:17 p.m., 2019-09-30] Mohammad: """Classes for representing nodes"""


class HuffmanNode:
    """ A node in a Huffman tree.
    Symbols occur only at leaves.
    Each node has a number attribute that can be used for node-numbering.

    Attributes:
    ===========
    @param int symbol: symbol located in this node, if any
    @param HuffmanNode left: left subtree
    @param HuffmanNode right: right subtree
    @param int number: node number
    """

    def _init_(self, symbol=None, left=None, right=None):
        """ Create a new HuffmanNode with the given parameters.

        @param HuffmanNode self: this HuffmanNode
        @param int|Node symbol: symbol to be stored in this node, if any
        @param HuffmanNode|Node left: a tree rooted at 'left', if any
        @param HuffmanNode|Node right: a tree rooted at 'right', if any
        @rtype: NoneType
        """
        self.symbol = symbol
        self.left, self.right = left, right
        self.number = None

    def _eq_(self, other):
        """ Return True iff self is equivalent to other.

        @param HuffmanNode self: this HuffmanNode tree
        @param HuffmanNode|Any other: a tree rooted at the HuffmanNode 'other'
        @rtype: bool

        >>> a = HuffmanNode(4)
        >>> b = HuffmanNode(4)
        >>> a == b
        True
        >>> b = HuffmanNode(5)
        >>> a == b
        False
        """
        return (type(self) == type(other) and self.symbol == other.symbol and
                self.left == other.left and self.right == other.right)

    def _lt_(self, other):
        """ Return True iff self is less than other.

        @param HuffmanNode self: this HuffmanNode tree
        @param HuffmanNode|Any other: a tree rooted at the HuffmanNode 'other'
        @rtype: bool
        """
        return False  # arbitrarily say that one node is never less than another

    def _repr_(self):
        """ Return constructor-style string representation.

        @param HuffmanNode self: this HuffmanNode tree
        @rtype: str
        """
        return 'HuffmanNode({}, {}, {})'.format(self.symbol,
                                                self.left, self.right)

    def is_leaf(self):
        """ Return True iff self is a leaf.

        @param HuffmanNode self: this HuffmanNode tree
        @rtype: bool

        >>> t = HuffmanNode(None)
        >>> t.is_leaf()
        True
        """
        return not self.left and not self.right


class ReadNode:
    """ A node as read from a compressed file.
    Each node consists of type and data information as described in the handout.
    This class offers a clean way to collect this information for each node.

    Attributes:
    ===========
    @param int l_type: 0/1 (if the corresponding HuffmanNode's left is a leaf)
    @param int l_data: a symbol or the node number of a HuffmanNode's left
    @param int r_type: 0/1 (if the corresponding HuffmanNode's right is a leaf)
    @param int r_data: a symbol or the node number of a HuffmanNode's right
    """

    def _init_(self, l_type, l_data, r_type, r_data):
        """ Create a new ReadNode with the given parameters.

        @param ReadNode self: this ReadNode
        @param int l_type: used to initialize self.l_type
        @param int l_data: used to initialize self.l_data
        @param int r_type: used to initialize self.r_type
        @param int r_data: used to initialize self.r_data
        @rtype: NoneType
        """
        self.l_type, self.l_data = l_type, l_data
        self.r_type, self.r_data = r_type, r_data

    def _repr_(self):
        """ Return constructor-style string representation.

        @param ReadNode self: this ReadNode
        @rtype: str
        """
        return 'ReadNode({}, {}, {}, {})'.format(
            self.l_type, self.l_data, self.r_type, self.r_data)

if _name_ == '_main_':
    import doctest
    doctest.testmod()

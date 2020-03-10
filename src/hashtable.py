# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        '''
        pair = LinkedPair(key, value)
        index = self._hash_mod(key)

        if self.storage[index]:
            pair.next = self.storage[index]
            self.storage[index] = pair
            current_pair = pair
            print("THIS IS THE LOOP FOR INDEX:", index)
            while current_pair:
                print(current_pair.key, current_pair.value)
                current_pair = current_pair.next
        else:
            self.storage[index] = pair
            print("INSERTED", key, "AT", index)

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        '''
        for i in range(self.capacity):
            print("------BOOGERS-------", i)
            print(len(self.storage))
            item = self.storage[i]

            if item:
                print("ENTERED LOOP READY TO REMOVE")
                print("HERES THE CURRENT ITEM", item.key, item.value)
                if item.key == key:
                    print("SHOULDNT HIT THIS")
                    self.storage = self.storage[0 : i] + self.storage[i + 1:]
                elif item.next:
                    print("SHOULD ENTER THIS")
                    current_pair = item
                    while current_pair:
                        print("HERES THE CURRENT ITEM", current_pair.value, current_pair.key)
                        if current_pair.key == key:
                            current_pair.key = None
                            current_pair.value = None
                            current_pair.next = None
                        current_pair = current_pair.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        '''
        for i in range(self.capacity):
            item = self.storage[i]
            # If the current item is not None
            if item:
                # If 'pair' key is equal to requested key, return the 'pair' value
                if item.key == key:
                    return item.value
                # If there is multiple pairs stored at the index, loop through them, and find the one requested
                elif item.next:
                    current_pair = item

                    while current_pair:
                        if current_pair.key == key:
                            return current_pair.value
                        current_pair = current_pair.next
        

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''

        self.capacity *= 2
        old_storage = [None] * self.capacity

        for i in range(len(self.storage)):
            old_storage[i] = self.storage[i]
        
        self.storage = old_storage


if __name__ == "__main__":
    ht = HashTable(8)

    ht.insert("key-0", "val-0")
    ht.insert("key-1", "val-1")
    ht.insert("key-2", "val-2")
    ht.insert("key-3", "val-3")
    ht.insert("key-4", "val-4")
    ht.insert("key-5", "val-5")
    ht.insert("key-6", "val-6")
    ht.insert("key-7", "val-7")
    # ht.insert("key-8", "val-8")
    # ht.insert("key-9", "val-9")

    return_value = ht.retrieve("key-0")
    print("YOUR RETUR NVALUE", return_value, "\n")
    return_value = ht.retrieve("key-1")
    print("YOUR RETUR NVALUE", return_value, "\n")
    return_value = ht.retrieve("key-2")
    print("YOUR RETUR NVALUE", return_value, "\n")
    return_value = ht.retrieve("key-3")
    print("YOUR RETUR NVALUE", return_value, "\n")
    return_value = ht.retrieve("key-4")
    print("YOUR RETUR NVALUE", return_value, "\n")
    return_value = ht.retrieve("key-5")
    print("YOUR RETUR NVALUE", return_value, "\n")
    return_value = ht.retrieve("key-6")
    print("YOUR RETUR NVALUE", return_value, "\n")
    return_value = ht.retrieve("key-7")
    print("YOUR RETUR NVALUE", return_value, "\n")
    # return_value = ht.retrieve("key-8")
    # print("YOUR RETUR NVALUE", return_value, "\n")
    ht.remove("key-7")
    # print("BOOGER", ht.retrieve("key-8"))
    # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    print("")

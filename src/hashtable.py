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

            current_pair = self.storage[index]

            while current_pair:
                current_pair = current_pair.next
        else:
            self.storage[index] = pair

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        '''
        index = self._hash_mod(key)
        item = self.storage[index]

        # If item exists...
        if item:
            # If it is part of a linked list, loop through the pairs, until you find the matching `key`
            if item.next:
                current_pair = item

                while current_pair:
                    if current_pair.key == key:
                        # Remove pointers
                        item = current_pair.next
                        current_pair.next = None
                    current_pair = current_pair.next
            else:
                # If it's not part of a linked list, set the value to None
                self.storage[index] = None

        else:
            print("That item don't exist dudeman")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        '''
        index = self._hash_mod(key)
        item = self.storage[index]
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
        else:
            return None
        

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''
        self.capacity *= 2
        old_storage = self.storage
        self.storage = [None] * self.capacity

        for pair in old_storage:
            current_pair = pair

            while current_pair:
                self.insert(current_pair.key, current_pair.value)
                current_pair = current_pair.next        


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
    ht.insert("key-8", "val-8")
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
    return_value = ht.retrieve("key-8")
    print("YOUR RETUR NVALUE", return_value, "\n")
    
    ht.remove("key-8")
    ht.remove("key-7")
    ht.remove("key-6")
    ht.remove("key-5")
    ht.remove("key-4")
    ht.remove("key-3")
    ht.remove("key-2")
    ht.remove("key-1")
    ht.remove("key-0")

    return_value = ht.retrieve("key-0")
    print("RETURN VALUE", return_value)
    return_value = ht.retrieve("key-1")
    print("RETURN VALUE", return_value)
    return_value = ht.retrieve("key-2")
    print("RETURN VALUE", return_value)
    return_value = ht.retrieve("key-3")
    print("RETURN VALUE", return_value)
    return_value = ht.retrieve("key-4")
    print("RETURN VALUE", return_value)
    return_value = ht.retrieve("key-5")
    print("RETURN VALUE", return_value)
    return_value = ht.retrieve("key-6")
    print("RETURN VALUE", return_value)
    return_value = ht.retrieve("key-7")
    print("RETURN VALUE", return_value)
    return_value = ht.retrieve("key-8")
    print("RETURN VALUE", return_value)
    
    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # print("")
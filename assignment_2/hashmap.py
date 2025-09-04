class HashMap:
    def __init__(self, size=10):
     
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

       
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        
        bucket.append([key, value])

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None  

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return True
        return False  



hm = HashMap()
hm.put("apple", 10)
hm.put("banana", 20)
hm.put("grape", 30)

print(hm.get("banana"))   
hm.remove("banana")
print(hm.get("banana"))   

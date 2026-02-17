class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
         txn1, txn2, txn3, ....
        | ------ 60 min ------ |
        
        while abs(txn1.time - new.time) > 60:
            queue.popleft()
        
        if new.amt > 1000:
            invalid.add(i)
        
        for txn in queue:
            if txn.name == new.name and txn.city != new.city:
                invalid.add(i)
                invalid.add(txn.i)
        
        """

        def parse(txn):
            name, time, amt, city = txn.split(',')
            return (name, int(time), int(amt), city, txn)

        txns = [ parse(txn) for txn in transactions ]
        txns.sort(key=lambda x: x[1])
        invalid = set()
        queue = deque()
        for i, txn in enumerate(txns):
            name, time, amt, city, _ = txn
            
            while queue and abs(time - queue[0][2]) > 60:
                queue.popleft()
            
            if amt > 1000:
                invalid.add(i)
            
            for txn in queue:
                if txn[1] == name and txn[3] != city:
                    invalid.add(txn[0])
                    invalid.add(i)
            
            queue.append((i, name, time, city))
        
        return [ txns[i][4] for i in invalid ]

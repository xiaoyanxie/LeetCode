from collections import deque
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # sort by time asc
        txns = []
        for tstr in transactions:
            name, time, amt, city = tstr.split(',')
            txns.append( (name, int(time), int(amt), city) )
        txns.sort(key=lambda txn: txn[1])

        # name -> [ idx1, idx2, ... ]
        window60min = defaultdict(deque)

        # if one txn is invalid, all txns within the 60 min window under same name but different city are also invalid 
        invalid = set()
        for idx, txn in enumerate(txns):
            name, time, amt, city = txn

            while window60min[name] and abs(time - txns[window60min[name][0]][1]) > 60:
                window60min[name].popleft()
            
            if amt > 1000:
                invalid.add(idx)
            
            for hidx in window60min[name]:
                history = txns[hidx]
                if city != history[3]:
                    invalid.add(idx)
                    invalid.add(hidx)
            
            window60min[name].append(idx)

        def tostr(txn):
            name, time, amt, city = txn
            return f'{name},{time},{amt},{city}'
        
        return [ tostr(txns[i]) for i in invalid ]

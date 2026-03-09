from collections import deque, defaultdict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        txn invalid if:
           amt > 1000
           txn.name occurs, txn.city different

        window: [ (name, time, city, idx) ]
        mapping: {
            name -> { (idx, city1), (idx, city2) }
        }

        "alice,20,800,mtv","alice,50,100,beijing"

        txns: [ (alice, 20, 800, mtv, 0), (alice, 80, 100, beijing, 1) ]
        window: (alice, 20, mtv, 0)
        mapping: {
            alice: { (0, mtv) }
        }


        "alice,20,800,mtv","alice,50,1200,mtv"
        
        txns: [ (alice, 20, 800, mtv, 0), (alice, 50, 1200, mtv, 1) ]
        window: (alice, 20, mtv, 0)
        mapping: {
            alice: { (0, mtv) }
        }
        """
        txns = []
        for i, txn in enumerate(transactions):
            name, time, amt, city = txn.split(',')
            txns.append((name, int(time), int(amt), city, i))

        txns.sort(key=lambda txn: txn[1])

        invalid = set()
        window = deque() # 60 min
        mapping = defaultdict(set)
        for name, time, amt, city, idx in txns: # alice, 50, 100, beijing, 1
            # print(f'checking: {name}, {time}, {amt}, {city}, {idx}')
            if amt > 1000:
                # print(f'invalid: {name} has amt={amt} > 1000')
                invalid.add(idx)

            while window and time - window[0][1] > 60:
                lname, _, lcity, lidx = window.popleft()
                assert lname in mapping and (lidx, lcity) in mapping[lname]
                mapping[lname].remove((lidx, lcity))
                if not mapping[lname]:
                    del mapping[lname]
            
            # print(f'window={window}, mapping={mapping}')
            if name in mapping:
                for otherIdx, otherCity in mapping[name]:
                    # same name, different city
                    if city != otherCity:
                        # print(f'invalid: {name} happened in both {city} and {otherCity}')
                        invalid.add(otherIdx)
                        invalid.add(idx)
            
            window.append((name, time, city, idx))
            mapping[name].add((idx, city))
        
        return [ transactions[i] for i in invalid ]

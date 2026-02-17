class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        
        # 1. Precompute Zero Indices
        # Add a "sentinel" zero at index 'n' so we don't need 'if' checks for the end of the string.
        zeros = [idx for idx, char in enumerate(s) if char == '0']
        zeros.append(n) 
        
        total_valid_substrings = 0
        
        # 'zero_ptr' tracks the first zero at or after our current starting position 'i'
        zero_ptr = 0
        
        # 2. Iterate Start Position (i)
        for i in range(n):
            # Ensure zero_ptr is always pointing to the next upcoming zero relative to i
            if zero_ptr < len(zeros) and zeros[zero_ptr] < i:
                zero_ptr += 1
            
            # 3. Iterate Zero Count (k) - The "Visual Jump"
            # We look at zones defined by: "What if the substring has k zeros?"
            # zone index j corresponds to the count of zeros 'k'
            for j in range(zero_ptr, len(zeros)):
                k = j - zero_ptr  # Count of zeros in this range
                
                # LOGIC: The "Zero Bottleneck"
                # If we have k zeros, we need at least k^2 ones.
                # If k^2 is greater than the entire remaining string, we can stop early.
                if k * k > n - i:
                    break
                
                # ZONE BOUNDARIES
                # A substring with exactly 'k' zeros must end:
                #  - AFTER the k-th zero (inclusive)
                #  - BEFORE the (k+1)-th zero (exclusive)
                
                # The "next zero" marks the hard stop for this zone.
                next_zero_idx = zeros[j]
                
                # CASE: k = 0 (Pure 1s)
                # Logic: Ends anywhere before the first zero.
                if k == 0:
                    # Valid endings are [i, next_zero_idx - 1]
                    # Since 0^2 = 0, all these have enough ones.
                    total_valid_substrings += (next_zero_idx - i)
                    continue
                
                # CASE: k > 0
                # Logic: Must end at least at the k-th zero to capture it.
                # The k-th zero is at zeros[j-1] because 'zeros[j]' is the boundary (k+1)-th zero.
                last_zero_idx = zeros[j-1]
                
                # CONSTRAINT: ones >= k^2
                # Length = zeros + ones = k + ones
                # So: Length >= k + k^2
                # end_idx - start_idx + 1 >= k + k^2
                # end_idx >= i + k + k^2 - 1
                min_end_idx = i + k + (k * k) - 1
                
                # The valid ending positions are the intersection of:
                # 1. Being inside the zone (between last_zero_idx and next_zero_idx)
                # 2. Being long enough (>= min_end_idx)
                
                valid_start = max(last_zero_idx, min_end_idx)
                valid_end = next_zero_idx - 1
                
                if valid_start <= valid_end:
                    total_valid_substrings += (valid_end - valid_start + 1)
                    
        return total_valid_substrings

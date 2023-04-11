def my_hash(input_str):
    # Convert input string to binary
    input_bin = ''.join(format(ord(c), '08b') for c in input_str)
    
    # Define initial values for hash
    h0 = 0x01234567
    h1 = 0x89abcdef
    h2 = 0xfedcba98
    h3 = 0x76543210
    
    # Define constants
    c1 = 0x5a827999
    c2 = 0x6ed9eba1
    
    # Split input into chunks of 32 bits
    chunks = [input_bin[i:i+32] for i in range(0, len(input_bin), 32)]
    
    # Apply hashing algorithm to each chunk
    for chunk in chunks:
        # Convert chunk to integer
        x = int(chunk, 2)
        
        # Apply logical operations
        a = h0
        b = h1
        c = h2
        d = h3
        
        a = (a + ((b & c) | ((~b) & d)) + x + c1) & 0xffffffff
        d = (d + ((a & b) | ((~a) & c)) + x + c2) & 0xffffffff
        c = (c + ((d & a) | ((~d) & b)) + x + c1) & 0xffffffff
        b = (b + ((c & d) | ((~c) & a)) + x + c2) & 0xffffffff
        
        # Update hash values
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        
    # Concatenate hash values and return as hex string
    return '%08x%08x%08x%08x' % (h0, h1, h2, h3)


# Get input from user
input_str = input("Enter string to hash: ")

# Calculate hash value using custom algorithm
hash_value = my_hash(input_str)

# Print hash value
print("Hash value: " + hash_value)

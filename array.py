from math import ceil

def unique_chars_hash(s):
    # Pg 90, Q1.1
    if len(s) > 128:
        return False

    chars = {}
    for char in s:
        try:
            if chars[char] == 1:
                return False
        except:
            chars[char] = 1
    return True

def unique_chars_bit_vec(s):
    # Pg 90, Q1.1
    if len(s) > 128:
        return False

    chars = [False] * 128
    for char in s:
        i = ord(char)
        if chars[i]:
            return False
        chars[i] = True
    return True

def unique_chars_nlogn(s):
    # Pg 90, Q1.1
    chars = []
    for char in s:
        chars.append(char)

    chars.sort()

    for i in range(len(s)-1):
        if chars[i] == chars[i+1]:
            return False
    return True

def is_permutation(s, t):
    if not len(s) == len(t):
        return False

    # Pg 90, Q1.2
    chars_s = [False] * 128
    chars_t = [False] * 128

    for char in s:
        i = ord(char)
        chars_s[i] += 1

    for char in t:
        i = ord(char)
        chars_t[i] += 1

    return chars_s == chars_t

def is_permutation_hash(s, t):
    # Pg 90, Q1.2
    if not len(s) == len(t):
        return False

    chars_s = chars_t = {}
    for char in s:
        try:
            chars_s[char] += 1
        except:
            chars_s[char] = 1

    for char in t:
        try:
            chars_t[char] += 1
        except:
            chars_t[char] = 1

    return chars_s == chars_t

def is_permutation_nlogn(s, t):
    # Pg 90, Q1.2
    if not len(s) == len(t):
        return False

    chars_s = []
    for char in s:
        chars_s.append(char)

    chars_t = []
    for char in t:
        chars_t.append(char)

    return chars_s.sort() == chars_t.sort()

def urlify(s, true_count):
    # Pg 90, Q1.3
    num_spaces = char_count(s[0:true_count], ' ')
    next_index = true_count - 1 + num_spaces * 2

    for i in range(true_count-1, 0, -1):
        if s[i] == ' ':
            s[next_index] = '0'
            s[next_index-1] = '2'
            s[next_index-2] = '%'

            next_index -= 3
        else:
            s[next_index] = s[i]
            next_index -= 1

def char_count(s, match):
    # Pg 90, Q1.3
    count = 0
    for char in s:
        if char == match:
            count += 1
    return count

def palindrome_permute(s):
    # Pg 91, Q1.4
    s = s.lower() # Ignore case
    chars = {}
    true_letter_count = 0

    # Get character counts
    for char in s:
        if not ord(char) in range(97,123): 
            # If the char is not a lower case letter, ignore it
            pass
        else:
            true_letter_count += 1
            try:
                chars[char] += 1
            except:
                chars[char] = 1
    
    # Make sure there is only 1 odd numbered count for an odd length
    odd_found = False
    for key in chars:
        count = chars[key]
        if count % 2 == 1 and odd_found:
            return False
        elif count % 2 == 1:
            odd_found = True
    return True

def palindrome_permute_optimized(s):
    # Pg 91, Q1.4
    s = s.lower() # Ignore case
    chars = {}
    true_letter_count = 0
    odds_count = 0

    # Get character counts
    for char in s:
        if not ord(char) in range(97,123): 
            # If the char is not a lower case letter, ignore it
            pass
        else:
            true_letter_count += 1
            try:
                chars[char] += 1

                # Update number of odd counts
                if chars[char] % 2 == 1:
                    odds_count += 1
                else:
                    odds_count -= 1
            except:
                chars[char] = 1

                # Update number of odd counts
                odds_count += 1
    return odds_count in [0,1]

def one_away(s, t):
    # Pg 91, Q1.5
    if len(s) + 1 == len(t):
        # If s has the extra letter, remove each char and search for a match
        return one_away_remove(t, s)

    elif len(s) == len(t) + 1:
        # If t has the extra letter, remove each char and search for a match
        return one_away_remove(s, t)
 
    elif len(s) == len(t):
        return one_away_replace(s, t)
    return False

def one_away_remove(first, second):
    # Pg 91, Q1.5
    for i in range(len(first)):
            if first[0:i] + first[i+1:] == second:
                return True
    return False

def one_away_replace(s, t):
    # Pg 91, Q1.5
    found_difference = False
    for i in range(len(s)):
        if (not s[i] == t[i]) and (not found_difference):
            # If we find a first difference, mark the flag
            found_difference = True
        elif not s[i] == t[i]:
            # If we find a second difference, return False
            return False
    return True

def string_compression(s):
    # Pg 91, Q1.6
    new_string = ''
    consecutive_count = 0

    for i in range(len(s)):
        consecutive_count += 1
        if i + 1 >= len(s) or (not s[i] == s[i+1]):
            # If the next char is different, append the char and count
            new_string += str(s[i]) + str(consecutive_count)
            consecutive_count = 0

    if len(new_string) >= len(s):
        return s
    return new_string

def string_compression_optimized(s):
    # Pg 91, Q1.6
    compressed_count = compress_count(s)
    if compressed_count > len(s):
        return s
    new_string = ''
    consecutive_count = 0

    for i in range(len(s)):
        consecutive_count += 1
        if i + 1 >= len(s) or (not s[i] == s[i+1]):
            # If the next char is different, append the char and count
            new_string += str(s[i]) + str(consecutive_count)
            consecutive_count = 0

    return new_string

def compress_count(s):
    # Pg 91, Q1.6
    compressed_len = 0
    consecutive_count = 0

    for i in range(len(s)):
        consecutive_count += 1
        if i + 1 >= len(s) or (not s[i] == s[i+1]):
            # If the next char is different, append the char and count
            compressed_len += 1 + len(str(consecutive_count))
            consecutive_count = 0

    return compressed_len

def rotate_matrix(m):
    # Pg 91, Q1.7
    layers = round(len(m) / 2)
    start = 0
    end = len(m) - 1
    
    if len(m) % 2 == 0:
        for i in range(layers, 0, -1):
            print("i is", i)
            for j in range(i + 1):
                if j == 1 and i == 1:
                    # Skip the last rotation for even length square
                    pass
                else:
                    rotate_corners(m, start, end, j)
            start += 1
            end -= 1
    else:
        for i in range(layers, 0, -1):
            for j in range(i):
                rotate_corners(m, start, end, j)
            start += 1
            end -= 1
    return m

def rotate_corners(m, start, end, offset = 0):
    # Pg 91, Q1.7
    temp1 = m[start + offset][end]
    m[start + offset][end] = m[start][start + offset]

    temp2 = m[end][end - offset]
    m[end][end - offset] = temp1

    temp3 = m[end - offset][start]
    m[end - offset][start] = temp2

    m[start][start + offset] = temp3

def zero_mat(m):
    # Pg 91, Q1.8
    zero_rows = []
    zero_cols = []
    for row in range(len(m)):
        for col in range(len(m[0])):
            if m[row][col] == 0:
                zero_rows.append(row)
                zero_cols.append(col)

    for row in zero_rows:
        for col in range(len(m[0])):
            m[row][col] = 0
    for col in zero_cols:
        for row in range(len(m)):
            m[row][col] = 0

    return m

def zero_mat_optimized(m):
    # Pg 91, Q1.7
    row_has_zero = False
    col_has_zero = False
    
    # Determine if first row has a zero
    for col in range(len(m[0])):
        if m[0][col] == 0:
            row_has_zero = True
            break
    
    # Determine if first column has a zero
    for row in range(len(m)):
        if m[row][0] == 0:
            col_has_zero = True
            break

    # Find other rows and columns with zeros
    for row in range(1, len(m)):
        for col in range(1, len(m[0])):
            if m[row][col] == 0:
                m[0][col] = 0
                m[row][0] = 0

    # Zero rows
    for row in range(1, len(m)):
        if m[row][0] == 0:
            zero_row(m, row)

    # Zero columns  
    for col in range(1, len(m[0])):
        if m[0][col] == 0:
            zero_col(m, col)

    # Final zero first row and column if necessary
    if row_has_zero:
        zero_row(m, 0)
    if col_has_zero:
        zero_col(m, 0)

    print(m)

def zero_row(m, row):
    # Pg 91, Q1.8
    for col in range(len(m[0])):
        m[row][col] = 0

def zero_col(m, col):
    # Pg 91, Q1.8
    for row in range(len(m)):
        m[row][col] = 0

def string_rotation(s, t):
    # Pg 91, Q1.9
    if s in t+t and len(s) == len(t) and len(s) > 0:
        return True
    return False

def main():
    s = "waterbottle"
    t = "bottlewaterbottle"
    print(string_rotation(s, t))
  
if __name__ == "__main__":
    main()



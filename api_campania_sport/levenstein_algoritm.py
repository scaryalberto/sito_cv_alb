# Calculates the Levenshtein distance between two strings
def levenshtein_distance(a, b):
    # If either array is empty, return the length of the other array
    if not len(a):
        return len(b)
    if not len(b):
        return len(a)

    # Check whether the last items are the same before testing the other items
    if a[-1] == b[-1]:
        cost = 0
    else:
        cost = 1

    return min(
        # Find the distance if an item in a is removed
        levenshtein_distance(a[:-1], b) + 1,
        # Find the distance if an item is removed from b (i.e. added to a)
        levenshtein_distance(a, b[:-1]) + 1,
        # Find the distance if an item is removed from a and b (i.e. substituted)
        levenshtein_distance(a[:-1], b[:-1]) + cost
    )

# A more optimized version of the Levenshtein distance function using an array of previously calculated distances
def opti_leven_distance(a, b):
    # Create an empty distance matrix with dimensions len(a)+1 x len(b)+1
    dists = [ [0 for _ in range(len(b)+1)] for _ in range(len(a)+1) ]

    # a's default distances are calculated by removing each character
    for i in range(1, len(a)+1):
        dists[i][0] = i
    # b's default distances are calulated by adding each character
    for j in range(1, len(b)+1):
        dists[0][j] = j

    # Find the remaining distances using previous distances
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            # Calculate the substitution cost
            if a[i-1] == b[j-1]:
                cost = 0
            else:
                cost = 1

            dists[i][j] = min(
                # Removing a character from a
                dists[i-1][j] + 1,
                # Adding a character to b
                dists[i][j-1] + 1,
                # Substituting a character from a to b
                dists[i-1][j-1] + cost
            )

    return dists[-1][-1]

# Function to test whether the distance function is working correctly
def test_distance(a, b, answer):
    dist = opti_leven_distance(a, b)

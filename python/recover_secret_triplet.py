def recover_secret(triplets):
    # Create a dictionary to store the position of each character
    # Initialize each character's position based on its first appearance
    output = {
        c: i
        for i, c in enumerate(set([item for sublist in triplets for item in sublist]))
    }

    # Flag to check if any swaps were made in the last iteration
    swaped = True

    # Continue looping until no swaps are made
    while swaped:
        swaped = False
        for triplet in triplets:
            # Ensure the order of characters in the triplet
            if output[triplet[0]] > output[triplet[1]]:
                # Swap positions if the order is incorrect
                output[triplet[0]], output[triplet[1]] = (
                    output[triplet[1]],
                    output[triplet[0]],
                )
                swaped = True
            if output[triplet[1]] > output[triplet[2]]:
                # Swap positions if the order is incorrect
                output[triplet[1]], output[triplet[2]] = (
                    output[triplet[2]],
                    output[triplet[1]],
                )
                swaped = True

    # Sort characters by their position
    temp = sorted(output.items(), key=lambda x: x[1])

    # Join sorted characters to form the secret
    return "".join([c for c, _ in temp])
